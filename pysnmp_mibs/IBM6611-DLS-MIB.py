_T='ibmdlsCirDestSap'
_S='ibmdlsCirDestAddress'
_R='ibmdlsCirSrcSap'
_Q='ibmdlsCirSrcAddress'
_P='ibmdlsCirIfIndex'
_O='ibmdlsStationAddress'
_N='ibmdlsStationIfIndex'
_M='ibmdlsDefaultNBDestName'
_L='ibmdlsDefaultDestAddress'
_K='ibmdlsRemoteNameFilterID'
_J='ibmdlsLocalNameFilterID'
_I='ibmdlsRemoteFrameFilterID'
_H='ibmdlsLocalFrameFilterID'
_G='ibmdlsRouterAddress'
_F='OctetString'
_E='DisplayString'
_D='IBM6611-DLS-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class FilterType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deny',1),('permit',2)))
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmProd_ObjectIdentity=ObjectIdentity
ibmProd=_IbmProd_ObjectIdentity((1,3,6,1,4,1,2,6))
_Ibm6611_ObjectIdentity=ObjectIdentity
ibm6611=_Ibm6611_ObjectIdentity((1,3,6,1,4,1,2,6,2))
_Ibmdls_ObjectIdentity=ObjectIdentity
ibmdls=_Ibmdls_ObjectIdentity((1,3,6,1,4,1,2,6,2,9))
class _IbmdlsVirtualRingSegmentNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_IbmdlsVirtualRingSegmentNumber_Type.__name__=_C
_IbmdlsVirtualRingSegmentNumber_Object=MibScalar
ibmdlsVirtualRingSegmentNumber=_IbmdlsVirtualRingSegmentNumber_Object((1,3,6,1,4,1,2,6,2,9,1),_IbmdlsVirtualRingSegmentNumber_Type())
ibmdlsVirtualRingSegmentNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsVirtualRingSegmentNumber.setStatus(_A)
_IbmdlsFrameFilterType_Type=FilterType
_IbmdlsFrameFilterType_Object=MibScalar
ibmdlsFrameFilterType=_IbmdlsFrameFilterType_Object((1,3,6,1,4,1,2,6,2,9,2),_IbmdlsFrameFilterType_Type())
ibmdlsFrameFilterType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsFrameFilterType.setStatus(_A)
_IbmdlsNameFilterType_Type=FilterType
_IbmdlsNameFilterType_Object=MibScalar
ibmdlsNameFilterType=_IbmdlsNameFilterType_Object((1,3,6,1,4,1,2,6,2,9,3),_IbmdlsNameFilterType_Type())
ibmdlsNameFilterType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsNameFilterType.setStatus(_A)
_IbmdlsRouterTable_Object=MibTable
ibmdlsRouterTable=_IbmdlsRouterTable_Object((1,3,6,1,4,1,2,6,2,9,4))
if mibBuilder.loadTexts:ibmdlsRouterTable.setStatus(_A)
_IbmdlsRouterEntry_Object=MibTableRow
ibmdlsRouterEntry=_IbmdlsRouterEntry_Object((1,3,6,1,4,1,2,6,2,9,4,1))
ibmdlsRouterEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:ibmdlsRouterEntry.setStatus(_A)
_IbmdlsRouterAddress_Type=IpAddress
_IbmdlsRouterAddress_Object=MibTableColumn
ibmdlsRouterAddress=_IbmdlsRouterAddress_Object((1,3,6,1,4,1,2,6,2,9,4,1,1),_IbmdlsRouterAddress_Type())
ibmdlsRouterAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsRouterAddress.setStatus(_A)
class _IbmdlsRouterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notActive',1),('active',2)))
_IbmdlsRouterStatus_Type.__name__=_C
_IbmdlsRouterStatus_Object=MibTableColumn
ibmdlsRouterStatus=_IbmdlsRouterStatus_Object((1,3,6,1,4,1,2,6,2,9,4,1,2),_IbmdlsRouterStatus_Type())
ibmdlsRouterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsRouterStatus.setStatus(_A)
class _IbmdlsRouterDefinedBy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('user',1),('system',2)))
_IbmdlsRouterDefinedBy_Type.__name__=_C
_IbmdlsRouterDefinedBy_Object=MibTableColumn
ibmdlsRouterDefinedBy=_IbmdlsRouterDefinedBy_Object((1,3,6,1,4,1,2,6,2,9,4,1,3),_IbmdlsRouterDefinedBy_Type())
ibmdlsRouterDefinedBy.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsRouterDefinedBy.setStatus(_A)
_IbmdlsLocalFrameFilterTable_Object=MibTable
ibmdlsLocalFrameFilterTable=_IbmdlsLocalFrameFilterTable_Object((1,3,6,1,4,1,2,6,2,9,5))
if mibBuilder.loadTexts:ibmdlsLocalFrameFilterTable.setStatus(_A)
_IbmdlsLocalFrameFilterEntry_Object=MibTableRow
ibmdlsLocalFrameFilterEntry=_IbmdlsLocalFrameFilterEntry_Object((1,3,6,1,4,1,2,6,2,9,5,1))
ibmdlsLocalFrameFilterEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:ibmdlsLocalFrameFilterEntry.setStatus(_A)
class _IbmdlsLocalFrameFilterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_IbmdlsLocalFrameFilterID_Type.__name__=_C
_IbmdlsLocalFrameFilterID_Object=MibTableColumn
ibmdlsLocalFrameFilterID=_IbmdlsLocalFrameFilterID_Object((1,3,6,1,4,1,2,6,2,9,5,1,1),_IbmdlsLocalFrameFilterID_Type())
ibmdlsLocalFrameFilterID.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsLocalFrameFilterID.setStatus(_A)
_IbmdlsLocalFrameFilterSrcAddress_Type=MacAddress
_IbmdlsLocalFrameFilterSrcAddress_Object=MibTableColumn
ibmdlsLocalFrameFilterSrcAddress=_IbmdlsLocalFrameFilterSrcAddress_Object((1,3,6,1,4,1,2,6,2,9,5,1,2),_IbmdlsLocalFrameFilterSrcAddress_Type())
ibmdlsLocalFrameFilterSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsLocalFrameFilterSrcAddress.setStatus(_A)
_IbmdlsLocalFrameFilterSrcMask_Type=MacAddress
_IbmdlsLocalFrameFilterSrcMask_Object=MibTableColumn
ibmdlsLocalFrameFilterSrcMask=_IbmdlsLocalFrameFilterSrcMask_Object((1,3,6,1,4,1,2,6,2,9,5,1,3),_IbmdlsLocalFrameFilterSrcMask_Type())
ibmdlsLocalFrameFilterSrcMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsLocalFrameFilterSrcMask.setStatus(_A)
_IbmdlsLocalFrameFilterDestAddress_Type=MacAddress
_IbmdlsLocalFrameFilterDestAddress_Object=MibTableColumn
ibmdlsLocalFrameFilterDestAddress=_IbmdlsLocalFrameFilterDestAddress_Object((1,3,6,1,4,1,2,6,2,9,5,1,4),_IbmdlsLocalFrameFilterDestAddress_Type())
ibmdlsLocalFrameFilterDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsLocalFrameFilterDestAddress.setStatus(_A)
_IbmdlsLocalFrameFilterDestMask_Type=MacAddress
_IbmdlsLocalFrameFilterDestMask_Object=MibTableColumn
ibmdlsLocalFrameFilterDestMask=_IbmdlsLocalFrameFilterDestMask_Object((1,3,6,1,4,1,2,6,2,9,5,1,5),_IbmdlsLocalFrameFilterDestMask_Type())
ibmdlsLocalFrameFilterDestMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsLocalFrameFilterDestMask.setStatus(_A)
_IbmdlsRemoteFrameFilterTable_Object=MibTable
ibmdlsRemoteFrameFilterTable=_IbmdlsRemoteFrameFilterTable_Object((1,3,6,1,4,1,2,6,2,9,6))
if mibBuilder.loadTexts:ibmdlsRemoteFrameFilterTable.setStatus(_A)
_IbmdlsRemoteFrameFilterEntry_Object=MibTableRow
ibmdlsRemoteFrameFilterEntry=_IbmdlsRemoteFrameFilterEntry_Object((1,3,6,1,4,1,2,6,2,9,6,1))
ibmdlsRemoteFrameFilterEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:ibmdlsRemoteFrameFilterEntry.setStatus(_A)
class _IbmdlsRemoteFrameFilterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_IbmdlsRemoteFrameFilterID_Type.__name__=_C
_IbmdlsRemoteFrameFilterID_Object=MibTableColumn
ibmdlsRemoteFrameFilterID=_IbmdlsRemoteFrameFilterID_Object((1,3,6,1,4,1,2,6,2,9,6,1,1),_IbmdlsRemoteFrameFilterID_Type())
ibmdlsRemoteFrameFilterID.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsRemoteFrameFilterID.setStatus(_A)
_IbmdlsRemoteFrameFilterSrcAddress_Type=MacAddress
_IbmdlsRemoteFrameFilterSrcAddress_Object=MibTableColumn
ibmdlsRemoteFrameFilterSrcAddress=_IbmdlsRemoteFrameFilterSrcAddress_Object((1,3,6,1,4,1,2,6,2,9,6,1,2),_IbmdlsRemoteFrameFilterSrcAddress_Type())
ibmdlsRemoteFrameFilterSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsRemoteFrameFilterSrcAddress.setStatus(_A)
_IbmdlsRemoteFrameFilterSrcMask_Type=MacAddress
_IbmdlsRemoteFrameFilterSrcMask_Object=MibTableColumn
ibmdlsRemoteFrameFilterSrcMask=_IbmdlsRemoteFrameFilterSrcMask_Object((1,3,6,1,4,1,2,6,2,9,6,1,3),_IbmdlsRemoteFrameFilterSrcMask_Type())
ibmdlsRemoteFrameFilterSrcMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsRemoteFrameFilterSrcMask.setStatus(_A)
_IbmdlsRemoteFrameFilterDestAddress_Type=MacAddress
_IbmdlsRemoteFrameFilterDestAddress_Object=MibTableColumn
ibmdlsRemoteFrameFilterDestAddress=_IbmdlsRemoteFrameFilterDestAddress_Object((1,3,6,1,4,1,2,6,2,9,6,1,4),_IbmdlsRemoteFrameFilterDestAddress_Type())
ibmdlsRemoteFrameFilterDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsRemoteFrameFilterDestAddress.setStatus(_A)
_IbmdlsRemoteFrameFilterDestMask_Type=MacAddress
_IbmdlsRemoteFrameFilterDestMask_Object=MibTableColumn
ibmdlsRemoteFrameFilterDestMask=_IbmdlsRemoteFrameFilterDestMask_Object((1,3,6,1,4,1,2,6,2,9,6,1,5),_IbmdlsRemoteFrameFilterDestMask_Type())
ibmdlsRemoteFrameFilterDestMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsRemoteFrameFilterDestMask.setStatus(_A)
_IbmdlsLocalNameFilterTable_Object=MibTable
ibmdlsLocalNameFilterTable=_IbmdlsLocalNameFilterTable_Object((1,3,6,1,4,1,2,6,2,9,7))
if mibBuilder.loadTexts:ibmdlsLocalNameFilterTable.setStatus(_A)
_IbmdlsLocalNameFilterEntry_Object=MibTableRow
ibmdlsLocalNameFilterEntry=_IbmdlsLocalNameFilterEntry_Object((1,3,6,1,4,1,2,6,2,9,7,1))
ibmdlsLocalNameFilterEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:ibmdlsLocalNameFilterEntry.setStatus(_A)
class _IbmdlsLocalNameFilterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_IbmdlsLocalNameFilterID_Type.__name__=_C
_IbmdlsLocalNameFilterID_Object=MibTableColumn
ibmdlsLocalNameFilterID=_IbmdlsLocalNameFilterID_Object((1,3,6,1,4,1,2,6,2,9,7,1,1),_IbmdlsLocalNameFilterID_Type())
ibmdlsLocalNameFilterID.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsLocalNameFilterID.setStatus(_A)
class _IbmdlsLocalNameFilterSrcAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_IbmdlsLocalNameFilterSrcAddress_Type.__name__=_E
_IbmdlsLocalNameFilterSrcAddress_Object=MibTableColumn
ibmdlsLocalNameFilterSrcAddress=_IbmdlsLocalNameFilterSrcAddress_Object((1,3,6,1,4,1,2,6,2,9,7,1,2),_IbmdlsLocalNameFilterSrcAddress_Type())
ibmdlsLocalNameFilterSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsLocalNameFilterSrcAddress.setStatus(_A)
class _IbmdlsLocalNameFilterDestAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_IbmdlsLocalNameFilterDestAddress_Type.__name__=_E
_IbmdlsLocalNameFilterDestAddress_Object=MibTableColumn
ibmdlsLocalNameFilterDestAddress=_IbmdlsLocalNameFilterDestAddress_Object((1,3,6,1,4,1,2,6,2,9,7,1,3),_IbmdlsLocalNameFilterDestAddress_Type())
ibmdlsLocalNameFilterDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsLocalNameFilterDestAddress.setStatus(_A)
_IbmdlsRemoteNameFilterTable_Object=MibTable
ibmdlsRemoteNameFilterTable=_IbmdlsRemoteNameFilterTable_Object((1,3,6,1,4,1,2,6,2,9,8))
if mibBuilder.loadTexts:ibmdlsRemoteNameFilterTable.setStatus(_A)
_IbmdlsRemoteNameFilterEntry_Object=MibTableRow
ibmdlsRemoteNameFilterEntry=_IbmdlsRemoteNameFilterEntry_Object((1,3,6,1,4,1,2,6,2,9,8,1))
ibmdlsRemoteNameFilterEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:ibmdlsRemoteNameFilterEntry.setStatus(_A)
class _IbmdlsRemoteNameFilterID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_IbmdlsRemoteNameFilterID_Type.__name__=_C
_IbmdlsRemoteNameFilterID_Object=MibTableColumn
ibmdlsRemoteNameFilterID=_IbmdlsRemoteNameFilterID_Object((1,3,6,1,4,1,2,6,2,9,8,1,1),_IbmdlsRemoteNameFilterID_Type())
ibmdlsRemoteNameFilterID.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsRemoteNameFilterID.setStatus(_A)
class _IbmdlsRemoteNameFilterSrcAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_IbmdlsRemoteNameFilterSrcAddress_Type.__name__=_E
_IbmdlsRemoteNameFilterSrcAddress_Object=MibTableColumn
ibmdlsRemoteNameFilterSrcAddress=_IbmdlsRemoteNameFilterSrcAddress_Object((1,3,6,1,4,1,2,6,2,9,8,1,2),_IbmdlsRemoteNameFilterSrcAddress_Type())
ibmdlsRemoteNameFilterSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsRemoteNameFilterSrcAddress.setStatus(_A)
class _IbmdlsRemoteNameFilterDestAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_IbmdlsRemoteNameFilterDestAddress_Type.__name__=_E
_IbmdlsRemoteNameFilterDestAddress_Object=MibTableColumn
ibmdlsRemoteNameFilterDestAddress=_IbmdlsRemoteNameFilterDestAddress_Object((1,3,6,1,4,1,2,6,2,9,8,1,3),_IbmdlsRemoteNameFilterDestAddress_Type())
ibmdlsRemoteNameFilterDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsRemoteNameFilterDestAddress.setStatus(_A)
_IbmdlsDefaultDestTable_Object=MibTable
ibmdlsDefaultDestTable=_IbmdlsDefaultDestTable_Object((1,3,6,1,4,1,2,6,2,9,9))
if mibBuilder.loadTexts:ibmdlsDefaultDestTable.setStatus(_A)
_IbmdlsDefaultDestEntry_Object=MibTableRow
ibmdlsDefaultDestEntry=_IbmdlsDefaultDestEntry_Object((1,3,6,1,4,1,2,6,2,9,9,1))
ibmdlsDefaultDestEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:ibmdlsDefaultDestEntry.setStatus(_A)
_IbmdlsDefaultDestAddress_Type=MacAddress
_IbmdlsDefaultDestAddress_Object=MibTableColumn
ibmdlsDefaultDestAddress=_IbmdlsDefaultDestAddress_Object((1,3,6,1,4,1,2,6,2,9,9,1,1),_IbmdlsDefaultDestAddress_Type())
ibmdlsDefaultDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsDefaultDestAddress.setStatus(_A)
_IbmdlsDefaultRouterAddress_Type=IpAddress
_IbmdlsDefaultRouterAddress_Object=MibTableColumn
ibmdlsDefaultRouterAddress=_IbmdlsDefaultRouterAddress_Object((1,3,6,1,4,1,2,6,2,9,9,1,2),_IbmdlsDefaultRouterAddress_Type())
ibmdlsDefaultRouterAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsDefaultRouterAddress.setStatus(_A)
_IbmdlsDefaultNBDestTable_Object=MibTable
ibmdlsDefaultNBDestTable=_IbmdlsDefaultNBDestTable_Object((1,3,6,1,4,1,2,6,2,9,10))
if mibBuilder.loadTexts:ibmdlsDefaultNBDestTable.setStatus(_A)
_IbmdlsDefaultNBDestEntry_Object=MibTableRow
ibmdlsDefaultNBDestEntry=_IbmdlsDefaultNBDestEntry_Object((1,3,6,1,4,1,2,6,2,9,10,1))
ibmdlsDefaultNBDestEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:ibmdlsDefaultNBDestEntry.setStatus(_A)
class _IbmdlsDefaultNBDestName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_IbmdlsDefaultNBDestName_Type.__name__=_E
_IbmdlsDefaultNBDestName_Object=MibTableColumn
ibmdlsDefaultNBDestName=_IbmdlsDefaultNBDestName_Object((1,3,6,1,4,1,2,6,2,9,10,1,1),_IbmdlsDefaultNBDestName_Type())
ibmdlsDefaultNBDestName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsDefaultNBDestName.setStatus(_A)
_IbmdlsDefaultNBRouterAddress_Type=IpAddress
_IbmdlsDefaultNBRouterAddress_Object=MibTableColumn
ibmdlsDefaultNBRouterAddress=_IbmdlsDefaultNBRouterAddress_Object((1,3,6,1,4,1,2,6,2,9,10,1,2),_IbmdlsDefaultNBRouterAddress_Type())
ibmdlsDefaultNBRouterAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsDefaultNBRouterAddress.setStatus(_A)
_IbmdlsStationTable_Object=MibTable
ibmdlsStationTable=_IbmdlsStationTable_Object((1,3,6,1,4,1,2,6,2,9,11))
if mibBuilder.loadTexts:ibmdlsStationTable.setStatus(_A)
_IbmdlsStationEntry_Object=MibTableRow
ibmdlsStationEntry=_IbmdlsStationEntry_Object((1,3,6,1,4,1,2,6,2,9,11,1))
ibmdlsStationEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:ibmdlsStationEntry.setStatus(_A)
_IbmdlsStationIfIndex_Type=Integer32
_IbmdlsStationIfIndex_Object=MibTableColumn
ibmdlsStationIfIndex=_IbmdlsStationIfIndex_Object((1,3,6,1,4,1,2,6,2,9,11,1,1),_IbmdlsStationIfIndex_Type())
ibmdlsStationIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationIfIndex.setStatus(_A)
class _IbmdlsStationAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IbmdlsStationAddress_Type.__name__=_C
_IbmdlsStationAddress_Object=MibTableColumn
ibmdlsStationAddress=_IbmdlsStationAddress_Object((1,3,6,1,4,1,2,6,2,9,11,1,2),_IbmdlsStationAddress_Type())
ibmdlsStationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationAddress.setStatus(_A)
class _IbmdlsStationTransmitWindowCount_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_IbmdlsStationTransmitWindowCount_Type.__name__=_C
_IbmdlsStationTransmitWindowCount_Object=MibTableColumn
ibmdlsStationTransmitWindowCount=_IbmdlsStationTransmitWindowCount_Object((1,3,6,1,4,1,2,6,2,9,11,1,3),_IbmdlsStationTransmitWindowCount_Type())
ibmdlsStationTransmitWindowCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationTransmitWindowCount.setStatus(_A)
class _IbmdlsStationRetransmitCount_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_IbmdlsStationRetransmitCount_Type.__name__=_C
_IbmdlsStationRetransmitCount_Object=MibTableColumn
ibmdlsStationRetransmitCount=_IbmdlsStationRetransmitCount_Object((1,3,6,1,4,1,2,6,2,9,11,1,4),_IbmdlsStationRetransmitCount_Type())
ibmdlsStationRetransmitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationRetransmitCount.setStatus(_A)
class _IbmdlsStationRetransmitThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_IbmdlsStationRetransmitThreshold_Type.__name__=_C
_IbmdlsStationRetransmitThreshold_Object=MibTableColumn
ibmdlsStationRetransmitThreshold=_IbmdlsStationRetransmitThreshold_Object((1,3,6,1,4,1,2,6,2,9,11,1,5),_IbmdlsStationRetransmitThreshold_Type())
ibmdlsStationRetransmitThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationRetransmitThreshold.setStatus(_A)
class _IbmdlsStationForceDisconnectTimeout_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_IbmdlsStationForceDisconnectTimeout_Type.__name__=_C
_IbmdlsStationForceDisconnectTimeout_Object=MibTableColumn
ibmdlsStationForceDisconnectTimeout=_IbmdlsStationForceDisconnectTimeout_Object((1,3,6,1,4,1,2,6,2,9,11,1,6),_IbmdlsStationForceDisconnectTimeout_Type())
ibmdlsStationForceDisconnectTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationForceDisconnectTimeout.setStatus(_A)
class _IbmdlsStationMaxIfieldSize_Type(Integer32):defaultValue=265;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(265,30729))
_IbmdlsStationMaxIfieldSize_Type.__name__=_C
_IbmdlsStationMaxIfieldSize_Object=MibTableColumn
ibmdlsStationMaxIfieldSize=_IbmdlsStationMaxIfieldSize_Object((1,3,6,1,4,1,2,6,2,9,11,1,7),_IbmdlsStationMaxIfieldSize_Type())
ibmdlsStationMaxIfieldSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationMaxIfieldSize.setStatus(_A)
class _IbmdlsStationPrimaryRepollTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250))
_IbmdlsStationPrimaryRepollTimeout_Type.__name__=_C
_IbmdlsStationPrimaryRepollTimeout_Object=MibTableColumn
ibmdlsStationPrimaryRepollTimeout=_IbmdlsStationPrimaryRepollTimeout_Object((1,3,6,1,4,1,2,6,2,9,11,1,8),_IbmdlsStationPrimaryRepollTimeout_Type())
ibmdlsStationPrimaryRepollTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationPrimaryRepollTimeout.setStatus(_A)
class _IbmdlsStationPrimaryRepollCount_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,50))
_IbmdlsStationPrimaryRepollCount_Type.__name__=_C
_IbmdlsStationPrimaryRepollCount_Object=MibTableColumn
ibmdlsStationPrimaryRepollCount=_IbmdlsStationPrimaryRepollCount_Object((1,3,6,1,4,1,2,6,2,9,11,1,9),_IbmdlsStationPrimaryRepollCount_Type())
ibmdlsStationPrimaryRepollCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationPrimaryRepollCount.setStatus(_A)
class _IbmdlsStationPrimaryRepollThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_IbmdlsStationPrimaryRepollThreshold_Type.__name__=_C
_IbmdlsStationPrimaryRepollThreshold_Object=MibTableColumn
ibmdlsStationPrimaryRepollThreshold=_IbmdlsStationPrimaryRepollThreshold_Object((1,3,6,1,4,1,2,6,2,9,11,1,10),_IbmdlsStationPrimaryRepollThreshold_Type())
ibmdlsStationPrimaryRepollThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationPrimaryRepollThreshold.setStatus(_A)
class _IbmdlsStationPrimarySlowListTimeout_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_IbmdlsStationPrimarySlowListTimeout_Type.__name__=_C
_IbmdlsStationPrimarySlowListTimeout_Object=MibTableColumn
ibmdlsStationPrimarySlowListTimeout=_IbmdlsStationPrimarySlowListTimeout_Object((1,3,6,1,4,1,2,6,2,9,11,1,11),_IbmdlsStationPrimarySlowListTimeout_Type())
ibmdlsStationPrimarySlowListTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationPrimarySlowListTimeout.setStatus(_A)
_IbmdlsStationSrcAddress_Type=MacAddress
_IbmdlsStationSrcAddress_Object=MibTableColumn
ibmdlsStationSrcAddress=_IbmdlsStationSrcAddress_Object((1,3,6,1,4,1,2,6,2,9,11,1,12),_IbmdlsStationSrcAddress_Type())
ibmdlsStationSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationSrcAddress.setStatus(_A)
_IbmdlsStationDestAddress_Type=MacAddress
_IbmdlsStationDestAddress_Object=MibTableColumn
ibmdlsStationDestAddress=_IbmdlsStationDestAddress_Object((1,3,6,1,4,1,2,6,2,9,11,1,13),_IbmdlsStationDestAddress_Type())
ibmdlsStationDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsStationDestAddress.setStatus(_A)
_IbmdlsCirTable_Object=MibTable
ibmdlsCirTable=_IbmdlsCirTable_Object((1,3,6,1,4,1,2,6,2,9,12))
if mibBuilder.loadTexts:ibmdlsCirTable.setStatus(_A)
_IbmdlsCirEntry_Object=MibTableRow
ibmdlsCirEntry=_IbmdlsCirEntry_Object((1,3,6,1,4,1,2,6,2,9,12,1))
ibmdlsCirEntry.setIndexNames((0,_D,_P),(0,_D,_Q),(0,_D,_R),(0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:ibmdlsCirEntry.setStatus(_A)
_IbmdlsCirIfIndex_Type=Integer32
_IbmdlsCirIfIndex_Object=MibTableColumn
ibmdlsCirIfIndex=_IbmdlsCirIfIndex_Object((1,3,6,1,4,1,2,6,2,9,12,1,1),_IbmdlsCirIfIndex_Type())
ibmdlsCirIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirIfIndex.setStatus(_A)
_IbmdlsCirSrcAddress_Type=MacAddress
_IbmdlsCirSrcAddress_Object=MibTableColumn
ibmdlsCirSrcAddress=_IbmdlsCirSrcAddress_Object((1,3,6,1,4,1,2,6,2,9,12,1,2),_IbmdlsCirSrcAddress_Type())
ibmdlsCirSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirSrcAddress.setStatus(_A)
_IbmdlsCirSrcSap_Type=Integer32
_IbmdlsCirSrcSap_Object=MibTableColumn
ibmdlsCirSrcSap=_IbmdlsCirSrcSap_Object((1,3,6,1,4,1,2,6,2,9,12,1,3),_IbmdlsCirSrcSap_Type())
ibmdlsCirSrcSap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirSrcSap.setStatus(_A)
_IbmdlsCirDestAddress_Type=MacAddress
_IbmdlsCirDestAddress_Object=MibTableColumn
ibmdlsCirDestAddress=_IbmdlsCirDestAddress_Object((1,3,6,1,4,1,2,6,2,9,12,1,4),_IbmdlsCirDestAddress_Type())
ibmdlsCirDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirDestAddress.setStatus(_A)
_IbmdlsCirDestSap_Type=Integer32
_IbmdlsCirDestSap_Object=MibTableColumn
ibmdlsCirDestSap=_IbmdlsCirDestSap_Object((1,3,6,1,4,1,2,6,2,9,12,1,5),_IbmdlsCirDestSap_Type())
ibmdlsCirDestSap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirDestSap.setStatus(_A)
_IbmdlsCirPartnerRouterAddress_Type=IpAddress
_IbmdlsCirPartnerRouterAddress_Object=MibTableColumn
ibmdlsCirPartnerRouterAddress=_IbmdlsCirPartnerRouterAddress_Object((1,3,6,1,4,1,2,6,2,9,12,1,6),_IbmdlsCirPartnerRouterAddress_Type())
ibmdlsCirPartnerRouterAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirPartnerRouterAddress.setStatus(_A)
class _IbmdlsCirLocalLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('opening',1),('opened',2),('closing',3),('inactive',4)))
_IbmdlsCirLocalLinkState_Type.__name__=_C
_IbmdlsCirLocalLinkState_Object=MibTableColumn
ibmdlsCirLocalLinkState=_IbmdlsCirLocalLinkState_Object((1,3,6,1,4,1,2,6,2,9,12,1,7),_IbmdlsCirLocalLinkState_Type())
ibmdlsCirLocalLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkState.setStatus(_A)
class _IbmdlsCirLocalLinkSubState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('calling',1),('listening',2),('contacted',3),('localBusy',4),('remoteBusy',5)))
_IbmdlsCirLocalLinkSubState_Type.__name__=_C
_IbmdlsCirLocalLinkSubState_Object=MibTableColumn
ibmdlsCirLocalLinkSubState=_IbmdlsCirLocalLinkSubState_Object((1,3,6,1,4,1,2,6,2,9,12,1,8),_IbmdlsCirLocalLinkSubState_Type())
ibmdlsCirLocalLinkSubState.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkSubState.setStatus(_A)
class _IbmdlsCirLocalLinkRouting_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,18))
_IbmdlsCirLocalLinkRouting_Type.__name__=_F
_IbmdlsCirLocalLinkRouting_Object=MibTableColumn
ibmdlsCirLocalLinkRouting=_IbmdlsCirLocalLinkRouting_Object((1,3,6,1,4,1,2,6,2,9,12,1,9),_IbmdlsCirLocalLinkRouting_Type())
ibmdlsCirLocalLinkRouting.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkRouting.setStatus(_A)
_IbmdlsCirLocalLinkTestCmdsSent_Type=Counter32
_IbmdlsCirLocalLinkTestCmdsSent_Object=MibTableColumn
ibmdlsCirLocalLinkTestCmdsSent=_IbmdlsCirLocalLinkTestCmdsSent_Object((1,3,6,1,4,1,2,6,2,9,12,1,10),_IbmdlsCirLocalLinkTestCmdsSent_Type())
ibmdlsCirLocalLinkTestCmdsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkTestCmdsSent.setStatus(_A)
_IbmdlsCirLocalLinkTestCmdsFail_Type=Counter32
_IbmdlsCirLocalLinkTestCmdsFail_Object=MibTableColumn
ibmdlsCirLocalLinkTestCmdsFail=_IbmdlsCirLocalLinkTestCmdsFail_Object((1,3,6,1,4,1,2,6,2,9,12,1,11),_IbmdlsCirLocalLinkTestCmdsFail_Type())
ibmdlsCirLocalLinkTestCmdsFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkTestCmdsFail.setStatus(_A)
_IbmdlsCirLocalLinkTestCmdsRcv_Type=Counter32
_IbmdlsCirLocalLinkTestCmdsRcv_Object=MibTableColumn
ibmdlsCirLocalLinkTestCmdsRcv=_IbmdlsCirLocalLinkTestCmdsRcv_Object((1,3,6,1,4,1,2,6,2,9,12,1,12),_IbmdlsCirLocalLinkTestCmdsRcv_Type())
ibmdlsCirLocalLinkTestCmdsRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkTestCmdsRcv.setStatus(_A)
_IbmdlsCirLocalLinkDataPktSent_Type=Counter32
_IbmdlsCirLocalLinkDataPktSent_Object=MibTableColumn
ibmdlsCirLocalLinkDataPktSent=_IbmdlsCirLocalLinkDataPktSent_Object((1,3,6,1,4,1,2,6,2,9,12,1,13),_IbmdlsCirLocalLinkDataPktSent_Type())
ibmdlsCirLocalLinkDataPktSent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkDataPktSent.setStatus(_A)
_IbmdlsCirLocalLinkDataPktResent_Type=Counter32
_IbmdlsCirLocalLinkDataPktResent_Object=MibTableColumn
ibmdlsCirLocalLinkDataPktResent=_IbmdlsCirLocalLinkDataPktResent_Object((1,3,6,1,4,1,2,6,2,9,12,1,14),_IbmdlsCirLocalLinkDataPktResent_Type())
ibmdlsCirLocalLinkDataPktResent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkDataPktResent.setStatus(_A)
_IbmdlsCirLocalLinkMaxContResent_Type=Counter32
_IbmdlsCirLocalLinkMaxContResent_Object=MibTableColumn
ibmdlsCirLocalLinkMaxContResent=_IbmdlsCirLocalLinkMaxContResent_Object((1,3,6,1,4,1,2,6,2,9,12,1,15),_IbmdlsCirLocalLinkMaxContResent_Type())
ibmdlsCirLocalLinkMaxContResent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkMaxContResent.setStatus(_A)
_IbmdlsCirLocalLinkDataPktRcv_Type=Counter32
_IbmdlsCirLocalLinkDataPktRcv_Object=MibTableColumn
ibmdlsCirLocalLinkDataPktRcv=_IbmdlsCirLocalLinkDataPktRcv_Object((1,3,6,1,4,1,2,6,2,9,12,1,16),_IbmdlsCirLocalLinkDataPktRcv_Type())
ibmdlsCirLocalLinkDataPktRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkDataPktRcv.setStatus(_A)
_IbmdlsCirLocalLinkInvalidPktRcv_Type=Counter32
_IbmdlsCirLocalLinkInvalidPktRcv_Object=MibTableColumn
ibmdlsCirLocalLinkInvalidPktRcv=_IbmdlsCirLocalLinkInvalidPktRcv_Object((1,3,6,1,4,1,2,6,2,9,12,1,17),_IbmdlsCirLocalLinkInvalidPktRcv_Type())
ibmdlsCirLocalLinkInvalidPktRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkInvalidPktRcv.setStatus(_A)
_IbmdlsCirLocalLinkAdpRcvErr_Type=Counter32
_IbmdlsCirLocalLinkAdpRcvErr_Object=MibTableColumn
ibmdlsCirLocalLinkAdpRcvErr=_IbmdlsCirLocalLinkAdpRcvErr_Object((1,3,6,1,4,1,2,6,2,9,12,1,18),_IbmdlsCirLocalLinkAdpRcvErr_Type())
ibmdlsCirLocalLinkAdpRcvErr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkAdpRcvErr.setStatus(_A)
_IbmdlsCirLocalLinkAdpSendErr_Type=Counter32
_IbmdlsCirLocalLinkAdpSendErr_Object=MibTableColumn
ibmdlsCirLocalLinkAdpSendErr=_IbmdlsCirLocalLinkAdpSendErr_Object((1,3,6,1,4,1,2,6,2,9,12,1,19),_IbmdlsCirLocalLinkAdpSendErr_Type())
ibmdlsCirLocalLinkAdpSendErr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkAdpSendErr.setStatus(_A)
_IbmdlsCirLocalLinkRcvInactiveTimeouts_Type=Counter32
_IbmdlsCirLocalLinkRcvInactiveTimeouts_Object=MibTableColumn
ibmdlsCirLocalLinkRcvInactiveTimeouts=_IbmdlsCirLocalLinkRcvInactiveTimeouts_Object((1,3,6,1,4,1,2,6,2,9,12,1,20),_IbmdlsCirLocalLinkRcvInactiveTimeouts_Type())
ibmdlsCirLocalLinkRcvInactiveTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkRcvInactiveTimeouts.setStatus(_A)
_IbmdlsCirLocalLinkCmdPollsSent_Type=Counter32
_IbmdlsCirLocalLinkCmdPollsSent_Object=MibTableColumn
ibmdlsCirLocalLinkCmdPollsSent=_IbmdlsCirLocalLinkCmdPollsSent_Object((1,3,6,1,4,1,2,6,2,9,12,1,21),_IbmdlsCirLocalLinkCmdPollsSent_Type())
ibmdlsCirLocalLinkCmdPollsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkCmdPollsSent.setStatus(_A)
_IbmdlsCirLocalLinkCmdRepollsSent_Type=Counter32
_IbmdlsCirLocalLinkCmdRepollsSent_Object=MibTableColumn
ibmdlsCirLocalLinkCmdRepollsSent=_IbmdlsCirLocalLinkCmdRepollsSent_Object((1,3,6,1,4,1,2,6,2,9,12,1,22),_IbmdlsCirLocalLinkCmdRepollsSent_Type())
ibmdlsCirLocalLinkCmdRepollsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkCmdRepollsSent.setStatus(_A)
_IbmdlsCirLocalLinkCmdContRepolls_Type=Counter32
_IbmdlsCirLocalLinkCmdContRepolls_Object=MibTableColumn
ibmdlsCirLocalLinkCmdContRepolls=_IbmdlsCirLocalLinkCmdContRepolls_Object((1,3,6,1,4,1,2,6,2,9,12,1,23),_IbmdlsCirLocalLinkCmdContRepolls_Type())
ibmdlsCirLocalLinkCmdContRepolls.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmdlsCirLocalLinkCmdContRepolls.setStatus(_A)
_Ibmappn_ObjectIdentity=ObjectIdentity
ibmappn=_Ibmappn_ObjectIdentity((1,3,6,1,4,1,2,6,2,13))
mibBuilder.exportSymbols(_D,**{'MacAddress':MacAddress,'FilterType':FilterType,'ibm':ibm,'ibmProd':ibmProd,'ibm6611':ibm6611,'ibmdls':ibmdls,'ibmdlsVirtualRingSegmentNumber':ibmdlsVirtualRingSegmentNumber,'ibmdlsFrameFilterType':ibmdlsFrameFilterType,'ibmdlsNameFilterType':ibmdlsNameFilterType,'ibmdlsRouterTable':ibmdlsRouterTable,'ibmdlsRouterEntry':ibmdlsRouterEntry,_G:ibmdlsRouterAddress,'ibmdlsRouterStatus':ibmdlsRouterStatus,'ibmdlsRouterDefinedBy':ibmdlsRouterDefinedBy,'ibmdlsLocalFrameFilterTable':ibmdlsLocalFrameFilterTable,'ibmdlsLocalFrameFilterEntry':ibmdlsLocalFrameFilterEntry,_H:ibmdlsLocalFrameFilterID,'ibmdlsLocalFrameFilterSrcAddress':ibmdlsLocalFrameFilterSrcAddress,'ibmdlsLocalFrameFilterSrcMask':ibmdlsLocalFrameFilterSrcMask,'ibmdlsLocalFrameFilterDestAddress':ibmdlsLocalFrameFilterDestAddress,'ibmdlsLocalFrameFilterDestMask':ibmdlsLocalFrameFilterDestMask,'ibmdlsRemoteFrameFilterTable':ibmdlsRemoteFrameFilterTable,'ibmdlsRemoteFrameFilterEntry':ibmdlsRemoteFrameFilterEntry,_I:ibmdlsRemoteFrameFilterID,'ibmdlsRemoteFrameFilterSrcAddress':ibmdlsRemoteFrameFilterSrcAddress,'ibmdlsRemoteFrameFilterSrcMask':ibmdlsRemoteFrameFilterSrcMask,'ibmdlsRemoteFrameFilterDestAddress':ibmdlsRemoteFrameFilterDestAddress,'ibmdlsRemoteFrameFilterDestMask':ibmdlsRemoteFrameFilterDestMask,'ibmdlsLocalNameFilterTable':ibmdlsLocalNameFilterTable,'ibmdlsLocalNameFilterEntry':ibmdlsLocalNameFilterEntry,_J:ibmdlsLocalNameFilterID,'ibmdlsLocalNameFilterSrcAddress':ibmdlsLocalNameFilterSrcAddress,'ibmdlsLocalNameFilterDestAddress':ibmdlsLocalNameFilterDestAddress,'ibmdlsRemoteNameFilterTable':ibmdlsRemoteNameFilterTable,'ibmdlsRemoteNameFilterEntry':ibmdlsRemoteNameFilterEntry,_K:ibmdlsRemoteNameFilterID,'ibmdlsRemoteNameFilterSrcAddress':ibmdlsRemoteNameFilterSrcAddress,'ibmdlsRemoteNameFilterDestAddress':ibmdlsRemoteNameFilterDestAddress,'ibmdlsDefaultDestTable':ibmdlsDefaultDestTable,'ibmdlsDefaultDestEntry':ibmdlsDefaultDestEntry,_L:ibmdlsDefaultDestAddress,'ibmdlsDefaultRouterAddress':ibmdlsDefaultRouterAddress,'ibmdlsDefaultNBDestTable':ibmdlsDefaultNBDestTable,'ibmdlsDefaultNBDestEntry':ibmdlsDefaultNBDestEntry,_M:ibmdlsDefaultNBDestName,'ibmdlsDefaultNBRouterAddress':ibmdlsDefaultNBRouterAddress,'ibmdlsStationTable':ibmdlsStationTable,'ibmdlsStationEntry':ibmdlsStationEntry,_N:ibmdlsStationIfIndex,_O:ibmdlsStationAddress,'ibmdlsStationTransmitWindowCount':ibmdlsStationTransmitWindowCount,'ibmdlsStationRetransmitCount':ibmdlsStationRetransmitCount,'ibmdlsStationRetransmitThreshold':ibmdlsStationRetransmitThreshold,'ibmdlsStationForceDisconnectTimeout':ibmdlsStationForceDisconnectTimeout,'ibmdlsStationMaxIfieldSize':ibmdlsStationMaxIfieldSize,'ibmdlsStationPrimaryRepollTimeout':ibmdlsStationPrimaryRepollTimeout,'ibmdlsStationPrimaryRepollCount':ibmdlsStationPrimaryRepollCount,'ibmdlsStationPrimaryRepollThreshold':ibmdlsStationPrimaryRepollThreshold,'ibmdlsStationPrimarySlowListTimeout':ibmdlsStationPrimarySlowListTimeout,'ibmdlsStationSrcAddress':ibmdlsStationSrcAddress,'ibmdlsStationDestAddress':ibmdlsStationDestAddress,'ibmdlsCirTable':ibmdlsCirTable,'ibmdlsCirEntry':ibmdlsCirEntry,_P:ibmdlsCirIfIndex,_Q:ibmdlsCirSrcAddress,_R:ibmdlsCirSrcSap,_S:ibmdlsCirDestAddress,_T:ibmdlsCirDestSap,'ibmdlsCirPartnerRouterAddress':ibmdlsCirPartnerRouterAddress,'ibmdlsCirLocalLinkState':ibmdlsCirLocalLinkState,'ibmdlsCirLocalLinkSubState':ibmdlsCirLocalLinkSubState,'ibmdlsCirLocalLinkRouting':ibmdlsCirLocalLinkRouting,'ibmdlsCirLocalLinkTestCmdsSent':ibmdlsCirLocalLinkTestCmdsSent,'ibmdlsCirLocalLinkTestCmdsFail':ibmdlsCirLocalLinkTestCmdsFail,'ibmdlsCirLocalLinkTestCmdsRcv':ibmdlsCirLocalLinkTestCmdsRcv,'ibmdlsCirLocalLinkDataPktSent':ibmdlsCirLocalLinkDataPktSent,'ibmdlsCirLocalLinkDataPktResent':ibmdlsCirLocalLinkDataPktResent,'ibmdlsCirLocalLinkMaxContResent':ibmdlsCirLocalLinkMaxContResent,'ibmdlsCirLocalLinkDataPktRcv':ibmdlsCirLocalLinkDataPktRcv,'ibmdlsCirLocalLinkInvalidPktRcv':ibmdlsCirLocalLinkInvalidPktRcv,'ibmdlsCirLocalLinkAdpRcvErr':ibmdlsCirLocalLinkAdpRcvErr,'ibmdlsCirLocalLinkAdpSendErr':ibmdlsCirLocalLinkAdpSendErr,'ibmdlsCirLocalLinkRcvInactiveTimeouts':ibmdlsCirLocalLinkRcvInactiveTimeouts,'ibmdlsCirLocalLinkCmdPollsSent':ibmdlsCirLocalLinkCmdPollsSent,'ibmdlsCirLocalLinkCmdRepollsSent':ibmdlsCirLocalLinkCmdRepollsSent,'ibmdlsCirLocalLinkCmdContRepolls':ibmdlsCirLocalLinkCmdContRepolls,'ibmappn':ibmappn})