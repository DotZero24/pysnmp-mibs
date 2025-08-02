_R='ibmfrBRSProtFiltId'
_Q='urgent'
_P='normal'
_O='read-write'
_N='DisplayString'
_M='IpAddress'
_L='Gauge32'
_K='Counter32'
_J='ibmfrBRSTrafficClassName'
_I='ibmfrBRSCircuitNumber'
_H='not-accessible'
_G='ibmfrBRSCircuitClassName'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='IBMFRBRS-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_K,'Counter64',_L,_D,_M,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
Counter32,Gauge32,Integer32,IpAddress=mibBuilder.importSymbols('SNMPv2-SMI-v1',_K,_L,_D,_M)
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention')
DisplayString,=mibBuilder.importSymbols('SNMPv2-TC-v1',_N)
_IbmfrBRS_ObjectIdentity=ObjectIdentity
ibmfrBRS=_IbmfrBRS_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,4,4))
_IbmfrBRSOperational_ObjectIdentity=ObjectIdentity
ibmfrBRSOperational=_IbmfrBRSOperational_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,4,4,1))
_IbmfrBRSInterfaceTable_Object=MibTable
ibmfrBRSInterfaceTable=_IbmfrBRSInterfaceTable_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,1))
if mibBuilder.loadTexts:ibmfrBRSInterfaceTable.setStatus(_A)
_IbmfrBRSInterfaceEntry_Object=MibTableRow
ibmfrBRSInterfaceEntry=_IbmfrBRSInterfaceEntry_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,1,1))
ibmfrBRSInterfaceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ibmfrBRSInterfaceEntry.setStatus(_A)
_IbmfrBRSInterfaceMaxQueue_Type=Integer32
_IbmfrBRSInterfaceMaxQueue_Object=MibTableColumn
ibmfrBRSInterfaceMaxQueue=_IbmfrBRSInterfaceMaxQueue_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,1,1,1),_IbmfrBRSInterfaceMaxQueue_Type())
ibmfrBRSInterfaceMaxQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSInterfaceMaxQueue.setStatus(_A)
_IbmfrBRSInterfaceMinQueue_Type=Integer32
_IbmfrBRSInterfaceMinQueue_Object=MibTableColumn
ibmfrBRSInterfaceMinQueue=_IbmfrBRSInterfaceMinQueue_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,1,1,2),_IbmfrBRSInterfaceMinQueue_Type())
ibmfrBRSInterfaceMinQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSInterfaceMinQueue.setStatus(_A)
_IbmfrBRSInterfaceTotalBandwidth_Type=Integer32
_IbmfrBRSInterfaceTotalBandwidth_Object=MibTableColumn
ibmfrBRSInterfaceTotalBandwidth=_IbmfrBRSInterfaceTotalBandwidth_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,1,1,3),_IbmfrBRSInterfaceTotalBandwidth_Type())
ibmfrBRSInterfaceTotalBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSInterfaceTotalBandwidth.setStatus(_A)
_IbmfrBRSInterfaceTotalCircuitClasses_Type=Integer32
_IbmfrBRSInterfaceTotalCircuitClasses_Object=MibTableColumn
ibmfrBRSInterfaceTotalCircuitClasses=_IbmfrBRSInterfaceTotalCircuitClasses_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,1,1,4),_IbmfrBRSInterfaceTotalCircuitClasses_Type())
ibmfrBRSInterfaceTotalCircuitClasses.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSInterfaceTotalCircuitClasses.setStatus(_A)
_IbmfrBRSInterfaceDefaultCircuitClassName_Type=DisplayString
_IbmfrBRSInterfaceDefaultCircuitClassName_Object=MibTableColumn
ibmfrBRSInterfaceDefaultCircuitClassName=_IbmfrBRSInterfaceDefaultCircuitClassName_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,1,1,5),_IbmfrBRSInterfaceDefaultCircuitClassName_Type())
ibmfrBRSInterfaceDefaultCircuitClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSInterfaceDefaultCircuitClassName.setStatus(_A)
_IbmfrBRSCircuitClassTable_Object=MibTable
ibmfrBRSCircuitClassTable=_IbmfrBRSCircuitClassTable_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,2))
if mibBuilder.loadTexts:ibmfrBRSCircuitClassTable.setStatus(_A)
_IbmfrBRSCircuitClassEntry_Object=MibTableRow
ibmfrBRSCircuitClassEntry=_IbmfrBRSCircuitClassEntry_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,2,1))
ibmfrBRSCircuitClassEntry.setIndexNames((0,_E,_F),(0,_C,_G))
if mibBuilder.loadTexts:ibmfrBRSCircuitClassEntry.setStatus(_A)
_IbmfrBRSCircuitClassName_Type=DisplayString
_IbmfrBRSCircuitClassName_Object=MibTableColumn
ibmfrBRSCircuitClassName=_IbmfrBRSCircuitClassName_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,2,1,1),_IbmfrBRSCircuitClassName_Type())
ibmfrBRSCircuitClassName.setMaxAccess(_H)
if mibBuilder.loadTexts:ibmfrBRSCircuitClassName.setStatus(_A)
_IbmfrBRSCircuitClassBandwidth_Type=Integer32
_IbmfrBRSCircuitClassBandwidth_Object=MibTableColumn
ibmfrBRSCircuitClassBandwidth=_IbmfrBRSCircuitClassBandwidth_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,2,1,2),_IbmfrBRSCircuitClassBandwidth_Type())
ibmfrBRSCircuitClassBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitClassBandwidth.setStatus(_A)
_IbmfrBRSCircuitClassPacketXmit_Type=Counter32
_IbmfrBRSCircuitClassPacketXmit_Object=MibTableColumn
ibmfrBRSCircuitClassPacketXmit=_IbmfrBRSCircuitClassPacketXmit_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,2,1,3),_IbmfrBRSCircuitClassPacketXmit_Type())
ibmfrBRSCircuitClassPacketXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitClassPacketXmit.setStatus(_A)
_IbmfrBRSCircuitClassBytesXmit_Type=Counter32
_IbmfrBRSCircuitClassBytesXmit_Object=MibTableColumn
ibmfrBRSCircuitClassBytesXmit=_IbmfrBRSCircuitClassBytesXmit_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,2,1,4),_IbmfrBRSCircuitClassBytesXmit_Type())
ibmfrBRSCircuitClassBytesXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitClassBytesXmit.setStatus(_A)
_IbmfrBRSCircuitClassBytesOverflow_Type=Counter32
_IbmfrBRSCircuitClassBytesOverflow_Object=MibTableColumn
ibmfrBRSCircuitClassBytesOverflow=_IbmfrBRSCircuitClassBytesOverflow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,2,1,5),_IbmfrBRSCircuitClassBytesOverflow_Type())
ibmfrBRSCircuitClassBytesOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitClassBytesOverflow.setStatus(_A)
_IbmfrBRSCircuitClassLastPacketXmit_Type=Counter32
_IbmfrBRSCircuitClassLastPacketXmit_Object=MibTableColumn
ibmfrBRSCircuitClassLastPacketXmit=_IbmfrBRSCircuitClassLastPacketXmit_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,2,1,6),_IbmfrBRSCircuitClassLastPacketXmit_Type())
ibmfrBRSCircuitClassLastPacketXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitClassLastPacketXmit.setStatus(_A)
_IbmfrBRSCircuitClassLastBytesXmit_Type=Counter32
_IbmfrBRSCircuitClassLastBytesXmit_Object=MibTableColumn
ibmfrBRSCircuitClassLastBytesXmit=_IbmfrBRSCircuitClassLastBytesXmit_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,2,1,7),_IbmfrBRSCircuitClassLastBytesXmit_Type())
ibmfrBRSCircuitClassLastBytesXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitClassLastBytesXmit.setStatus(_A)
_IbmfrBRSCircuitClassLastBytesOverflow_Type=Counter32
_IbmfrBRSCircuitClassLastBytesOverflow_Object=MibTableColumn
ibmfrBRSCircuitClassLastBytesOverflow=_IbmfrBRSCircuitClassLastBytesOverflow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,2,1,8),_IbmfrBRSCircuitClassLastBytesOverflow_Type())
ibmfrBRSCircuitClassLastBytesOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitClassLastBytesOverflow.setStatus(_A)
class _IbmfrBRSCircuitClassClearCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_IbmfrBRSCircuitClassClearCounters_Type.__name__=_D
_IbmfrBRSCircuitClassClearCounters_Object=MibTableColumn
ibmfrBRSCircuitClassClearCounters=_IbmfrBRSCircuitClassClearCounters_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,2,1,9),_IbmfrBRSCircuitClassClearCounters_Type())
ibmfrBRSCircuitClassClearCounters.setMaxAccess(_O)
if mibBuilder.loadTexts:ibmfrBRSCircuitClassClearCounters.setStatus(_A)
_IbmfrBRSCircuitTable_Object=MibTable
ibmfrBRSCircuitTable=_IbmfrBRSCircuitTable_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,3))
if mibBuilder.loadTexts:ibmfrBRSCircuitTable.setStatus(_A)
_IbmfrBRSCircuitEntry_Object=MibTableRow
ibmfrBRSCircuitEntry=_IbmfrBRSCircuitEntry_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,3,1))
ibmfrBRSCircuitEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_I))
if mibBuilder.loadTexts:ibmfrBRSCircuitEntry.setStatus(_A)
_IbmfrBRSCircuitNumber_Type=Integer32
_IbmfrBRSCircuitNumber_Object=MibTableColumn
ibmfrBRSCircuitNumber=_IbmfrBRSCircuitNumber_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,3,1,1),_IbmfrBRSCircuitNumber_Type())
ibmfrBRSCircuitNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:ibmfrBRSCircuitNumber.setStatus(_A)
_IbmfrBRSCircuitMaxQueue_Type=Integer32
_IbmfrBRSCircuitMaxQueue_Object=MibTableColumn
ibmfrBRSCircuitMaxQueue=_IbmfrBRSCircuitMaxQueue_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,3,1,2),_IbmfrBRSCircuitMaxQueue_Type())
ibmfrBRSCircuitMaxQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitMaxQueue.setStatus(_A)
_IbmfrBRSCircuitMinQueue_Type=Integer32
_IbmfrBRSCircuitMinQueue_Object=MibTableColumn
ibmfrBRSCircuitMinQueue=_IbmfrBRSCircuitMinQueue_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,3,1,3),_IbmfrBRSCircuitMinQueue_Type())
ibmfrBRSCircuitMinQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitMinQueue.setStatus(_A)
_IbmfrBRSCircuitTotalBandwidth_Type=Integer32
_IbmfrBRSCircuitTotalBandwidth_Object=MibTableColumn
ibmfrBRSCircuitTotalBandwidth=_IbmfrBRSCircuitTotalBandwidth_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,3,1,4),_IbmfrBRSCircuitTotalBandwidth_Type())
ibmfrBRSCircuitTotalBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitTotalBandwidth.setStatus(_A)
_IbmfrBRSCircuitTotalTrafficClasses_Type=Integer32
_IbmfrBRSCircuitTotalTrafficClasses_Object=MibTableColumn
ibmfrBRSCircuitTotalTrafficClasses=_IbmfrBRSCircuitTotalTrafficClasses_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,3,1,5),_IbmfrBRSCircuitTotalTrafficClasses_Type())
ibmfrBRSCircuitTotalTrafficClasses.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitTotalTrafficClasses.setStatus(_A)
_IbmfrBRSCircuitDefaultTrafficClassName_Type=DisplayString
_IbmfrBRSCircuitDefaultTrafficClassName_Object=MibTableColumn
ibmfrBRSCircuitDefaultTrafficClassName=_IbmfrBRSCircuitDefaultTrafficClassName_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,3,1,6),_IbmfrBRSCircuitDefaultTrafficClassName_Type())
ibmfrBRSCircuitDefaultTrafficClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitDefaultTrafficClassName.setStatus(_A)
class _IbmfrBRSCircuitDefaultTrafficClassPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),(_P,2),('high',3),(_Q,4)))
_IbmfrBRSCircuitDefaultTrafficClassPrio_Type.__name__=_D
_IbmfrBRSCircuitDefaultTrafficClassPrio_Object=MibTableColumn
ibmfrBRSCircuitDefaultTrafficClassPrio=_IbmfrBRSCircuitDefaultTrafficClassPrio_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,3,1,7),_IbmfrBRSCircuitDefaultTrafficClassPrio_Type())
ibmfrBRSCircuitDefaultTrafficClassPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitDefaultTrafficClassPrio.setStatus(_A)
class _IbmfrBRSCircuitSpecification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('defaults',1),('specific',2)))
_IbmfrBRSCircuitSpecification_Type.__name__=_D
_IbmfrBRSCircuitSpecification_Object=MibTableColumn
ibmfrBRSCircuitSpecification=_IbmfrBRSCircuitSpecification_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,3,1,8),_IbmfrBRSCircuitSpecification_Type())
ibmfrBRSCircuitSpecification.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitSpecification.setStatus(_A)
_IbmfrBRSCircuitSuperClassName_Type=DisplayString
_IbmfrBRSCircuitSuperClassName_Object=MibTableColumn
ibmfrBRSCircuitSuperClassName=_IbmfrBRSCircuitSuperClassName_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,3,1,9),_IbmfrBRSCircuitSuperClassName_Type())
ibmfrBRSCircuitSuperClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitSuperClassName.setStatus(_A)
_IbmfrBRSCircuitSVCName_Type=DisplayString
_IbmfrBRSCircuitSVCName_Object=MibTableColumn
ibmfrBRSCircuitSVCName=_IbmfrBRSCircuitSVCName_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,3,1,10),_IbmfrBRSCircuitSVCName_Type())
ibmfrBRSCircuitSVCName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSCircuitSVCName.setStatus(_A)
_IbmfrBRSTrafficClassTable_Object=MibTable
ibmfrBRSTrafficClassTable=_IbmfrBRSTrafficClassTable_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4))
if mibBuilder.loadTexts:ibmfrBRSTrafficClassTable.setStatus(_A)
_IbmfrBRSTrafficClassEntry_Object=MibTableRow
ibmfrBRSTrafficClassEntry=_IbmfrBRSTrafficClassEntry_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1))
ibmfrBRSTrafficClassEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:ibmfrBRSTrafficClassEntry.setStatus(_A)
_IbmfrBRSTrafficClassName_Type=DisplayString
_IbmfrBRSTrafficClassName_Object=MibTableColumn
ibmfrBRSTrafficClassName=_IbmfrBRSTrafficClassName_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,1),_IbmfrBRSTrafficClassName_Type())
ibmfrBRSTrafficClassName.setMaxAccess(_H)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassName.setStatus(_A)
_IbmfrBRSTrafficClassBandwidth_Type=Integer32
_IbmfrBRSTrafficClassBandwidth_Object=MibTableColumn
ibmfrBRSTrafficClassBandwidth=_IbmfrBRSTrafficClassBandwidth_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,2),_IbmfrBRSTrafficClassBandwidth_Type())
ibmfrBRSTrafficClassBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassBandwidth.setStatus(_A)
_IbmfrBRSTrafficClassTotalPacketXmit_Type=Counter32
_IbmfrBRSTrafficClassTotalPacketXmit_Object=MibTableColumn
ibmfrBRSTrafficClassTotalPacketXmit=_IbmfrBRSTrafficClassTotalPacketXmit_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,3),_IbmfrBRSTrafficClassTotalPacketXmit_Type())
ibmfrBRSTrafficClassTotalPacketXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassTotalPacketXmit.setStatus(_A)
_IbmfrBRSTrafficClassPacketXmitLow_Type=Counter32
_IbmfrBRSTrafficClassPacketXmitLow_Object=MibTableColumn
ibmfrBRSTrafficClassPacketXmitLow=_IbmfrBRSTrafficClassPacketXmitLow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,4),_IbmfrBRSTrafficClassPacketXmitLow_Type())
ibmfrBRSTrafficClassPacketXmitLow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassPacketXmitLow.setStatus(_A)
_IbmfrBRSTrafficClassPacketXmitNormal_Type=Counter32
_IbmfrBRSTrafficClassPacketXmitNormal_Object=MibTableColumn
ibmfrBRSTrafficClassPacketXmitNormal=_IbmfrBRSTrafficClassPacketXmitNormal_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,5),_IbmfrBRSTrafficClassPacketXmitNormal_Type())
ibmfrBRSTrafficClassPacketXmitNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassPacketXmitNormal.setStatus(_A)
_IbmfrBRSTrafficClassPacketXmitHigh_Type=Counter32
_IbmfrBRSTrafficClassPacketXmitHigh_Object=MibTableColumn
ibmfrBRSTrafficClassPacketXmitHigh=_IbmfrBRSTrafficClassPacketXmitHigh_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,6),_IbmfrBRSTrafficClassPacketXmitHigh_Type())
ibmfrBRSTrafficClassPacketXmitHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassPacketXmitHigh.setStatus(_A)
_IbmfrBRSTrafficClassPacketXmitUrgent_Type=Counter32
_IbmfrBRSTrafficClassPacketXmitUrgent_Object=MibTableColumn
ibmfrBRSTrafficClassPacketXmitUrgent=_IbmfrBRSTrafficClassPacketXmitUrgent_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,7),_IbmfrBRSTrafficClassPacketXmitUrgent_Type())
ibmfrBRSTrafficClassPacketXmitUrgent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassPacketXmitUrgent.setStatus(_A)
_IbmfrBRSTrafficClassTotalBytesXmit_Type=Counter32
_IbmfrBRSTrafficClassTotalBytesXmit_Object=MibTableColumn
ibmfrBRSTrafficClassTotalBytesXmit=_IbmfrBRSTrafficClassTotalBytesXmit_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,8),_IbmfrBRSTrafficClassTotalBytesXmit_Type())
ibmfrBRSTrafficClassTotalBytesXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassTotalBytesXmit.setStatus(_A)
_IbmfrBRSTrafficClassBytesXmitLow_Type=Counter32
_IbmfrBRSTrafficClassBytesXmitLow_Object=MibTableColumn
ibmfrBRSTrafficClassBytesXmitLow=_IbmfrBRSTrafficClassBytesXmitLow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,9),_IbmfrBRSTrafficClassBytesXmitLow_Type())
ibmfrBRSTrafficClassBytesXmitLow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassBytesXmitLow.setStatus(_A)
_IbmfrBRSTrafficClassBytesXmitNormal_Type=Counter32
_IbmfrBRSTrafficClassBytesXmitNormal_Object=MibTableColumn
ibmfrBRSTrafficClassBytesXmitNormal=_IbmfrBRSTrafficClassBytesXmitNormal_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,10),_IbmfrBRSTrafficClassBytesXmitNormal_Type())
ibmfrBRSTrafficClassBytesXmitNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassBytesXmitNormal.setStatus(_A)
_IbmfrBRSTrafficClassBytesXmitHigh_Type=Counter32
_IbmfrBRSTrafficClassBytesXmitHigh_Object=MibTableColumn
ibmfrBRSTrafficClassBytesXmitHigh=_IbmfrBRSTrafficClassBytesXmitHigh_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,11),_IbmfrBRSTrafficClassBytesXmitHigh_Type())
ibmfrBRSTrafficClassBytesXmitHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassBytesXmitHigh.setStatus(_A)
_IbmfrBRSTrafficClassBytesXmitUrgent_Type=Counter32
_IbmfrBRSTrafficClassBytesXmitUrgent_Object=MibTableColumn
ibmfrBRSTrafficClassBytesXmitUrgent=_IbmfrBRSTrafficClassBytesXmitUrgent_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,12),_IbmfrBRSTrafficClassBytesXmitUrgent_Type())
ibmfrBRSTrafficClassBytesXmitUrgent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassBytesXmitUrgent.setStatus(_A)
_IbmfrBRSTrafficClassTotalBytesOverflow_Type=Counter32
_IbmfrBRSTrafficClassTotalBytesOverflow_Object=MibTableColumn
ibmfrBRSTrafficClassTotalBytesOverflow=_IbmfrBRSTrafficClassTotalBytesOverflow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,13),_IbmfrBRSTrafficClassTotalBytesOverflow_Type())
ibmfrBRSTrafficClassTotalBytesOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassTotalBytesOverflow.setStatus(_A)
_IbmfrBRSTrafficClassBytesOverflowLow_Type=Counter32
_IbmfrBRSTrafficClassBytesOverflowLow_Object=MibTableColumn
ibmfrBRSTrafficClassBytesOverflowLow=_IbmfrBRSTrafficClassBytesOverflowLow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,14),_IbmfrBRSTrafficClassBytesOverflowLow_Type())
ibmfrBRSTrafficClassBytesOverflowLow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassBytesOverflowLow.setStatus(_A)
_IbmfrBRSTrafficClassBytesOverflowNormal_Type=Counter32
_IbmfrBRSTrafficClassBytesOverflowNormal_Object=MibTableColumn
ibmfrBRSTrafficClassBytesOverflowNormal=_IbmfrBRSTrafficClassBytesOverflowNormal_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,15),_IbmfrBRSTrafficClassBytesOverflowNormal_Type())
ibmfrBRSTrafficClassBytesOverflowNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassBytesOverflowNormal.setStatus(_A)
_IbmfrBRSTrafficClassBytesOverflowHigh_Type=Counter32
_IbmfrBRSTrafficClassBytesOverflowHigh_Object=MibTableColumn
ibmfrBRSTrafficClassBytesOverflowHigh=_IbmfrBRSTrafficClassBytesOverflowHigh_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,16),_IbmfrBRSTrafficClassBytesOverflowHigh_Type())
ibmfrBRSTrafficClassBytesOverflowHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassBytesOverflowHigh.setStatus(_A)
_IbmfrBRSTrafficClassBytesOverflowUrgent_Type=Counter32
_IbmfrBRSTrafficClassBytesOverflowUrgent_Object=MibTableColumn
ibmfrBRSTrafficClassBytesOverflowUrgent=_IbmfrBRSTrafficClassBytesOverflowUrgent_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,17),_IbmfrBRSTrafficClassBytesOverflowUrgent_Type())
ibmfrBRSTrafficClassBytesOverflowUrgent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassBytesOverflowUrgent.setStatus(_A)
_IbmfrBRSTrafficClassTotalPacketOverflow_Type=Counter32
_IbmfrBRSTrafficClassTotalPacketOverflow_Object=MibTableColumn
ibmfrBRSTrafficClassTotalPacketOverflow=_IbmfrBRSTrafficClassTotalPacketOverflow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,18),_IbmfrBRSTrafficClassTotalPacketOverflow_Type())
ibmfrBRSTrafficClassTotalPacketOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassTotalPacketOverflow.setStatus(_A)
_IbmfrBRSTrafficClassPacketOverflowLow_Type=Counter32
_IbmfrBRSTrafficClassPacketOverflowLow_Object=MibTableColumn
ibmfrBRSTrafficClassPacketOverflowLow=_IbmfrBRSTrafficClassPacketOverflowLow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,19),_IbmfrBRSTrafficClassPacketOverflowLow_Type())
ibmfrBRSTrafficClassPacketOverflowLow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassPacketOverflowLow.setStatus(_A)
_IbmfrBRSTrafficClassPacketOverflowNormal_Type=Counter32
_IbmfrBRSTrafficClassPacketOverflowNormal_Object=MibTableColumn
ibmfrBRSTrafficClassPacketOverflowNormal=_IbmfrBRSTrafficClassPacketOverflowNormal_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,20),_IbmfrBRSTrafficClassPacketOverflowNormal_Type())
ibmfrBRSTrafficClassPacketOverflowNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassPacketOverflowNormal.setStatus(_A)
_IbmfrBRSTrafficClassPacketOverflowHigh_Type=Counter32
_IbmfrBRSTrafficClassPacketOverflowHigh_Object=MibTableColumn
ibmfrBRSTrafficClassPacketOverflowHigh=_IbmfrBRSTrafficClassPacketOverflowHigh_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,21),_IbmfrBRSTrafficClassPacketOverflowHigh_Type())
ibmfrBRSTrafficClassPacketOverflowHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassPacketOverflowHigh.setStatus(_A)
_IbmfrBRSTrafficClassPacketOverflowUrgent_Type=Counter32
_IbmfrBRSTrafficClassPacketOverflowUrgent_Object=MibTableColumn
ibmfrBRSTrafficClassPacketOverflowUrgent=_IbmfrBRSTrafficClassPacketOverflowUrgent_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,22),_IbmfrBRSTrafficClassPacketOverflowUrgent_Type())
ibmfrBRSTrafficClassPacketOverflowUrgent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassPacketOverflowUrgent.setStatus(_A)
_IbmfrBRSTrafficClassTotalLastPacketXmit_Type=Counter32
_IbmfrBRSTrafficClassTotalLastPacketXmit_Object=MibTableColumn
ibmfrBRSTrafficClassTotalLastPacketXmit=_IbmfrBRSTrafficClassTotalLastPacketXmit_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,23),_IbmfrBRSTrafficClassTotalLastPacketXmit_Type())
ibmfrBRSTrafficClassTotalLastPacketXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassTotalLastPacketXmit.setStatus(_A)
_IbmfrBRSTrafficClassLastPacketXmitLow_Type=Counter32
_IbmfrBRSTrafficClassLastPacketXmitLow_Object=MibTableColumn
ibmfrBRSTrafficClassLastPacketXmitLow=_IbmfrBRSTrafficClassLastPacketXmitLow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,24),_IbmfrBRSTrafficClassLastPacketXmitLow_Type())
ibmfrBRSTrafficClassLastPacketXmitLow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastPacketXmitLow.setStatus(_A)
_IbmfrBRSTrafficClassLastPacketXmitNormal_Type=Counter32
_IbmfrBRSTrafficClassLastPacketXmitNormal_Object=MibTableColumn
ibmfrBRSTrafficClassLastPacketXmitNormal=_IbmfrBRSTrafficClassLastPacketXmitNormal_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,25),_IbmfrBRSTrafficClassLastPacketXmitNormal_Type())
ibmfrBRSTrafficClassLastPacketXmitNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastPacketXmitNormal.setStatus(_A)
_IbmfrBRSTrafficClassLastPacketXmitHigh_Type=Counter32
_IbmfrBRSTrafficClassLastPacketXmitHigh_Object=MibTableColumn
ibmfrBRSTrafficClassLastPacketXmitHigh=_IbmfrBRSTrafficClassLastPacketXmitHigh_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,26),_IbmfrBRSTrafficClassLastPacketXmitHigh_Type())
ibmfrBRSTrafficClassLastPacketXmitHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastPacketXmitHigh.setStatus(_A)
_IbmfrBRSTrafficClassLastPacketXmitUrgent_Type=Counter32
_IbmfrBRSTrafficClassLastPacketXmitUrgent_Object=MibTableColumn
ibmfrBRSTrafficClassLastPacketXmitUrgent=_IbmfrBRSTrafficClassLastPacketXmitUrgent_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,27),_IbmfrBRSTrafficClassLastPacketXmitUrgent_Type())
ibmfrBRSTrafficClassLastPacketXmitUrgent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastPacketXmitUrgent.setStatus(_A)
_IbmfrBRSTrafficClassTotalLastBytesXmit_Type=Counter32
_IbmfrBRSTrafficClassTotalLastBytesXmit_Object=MibTableColumn
ibmfrBRSTrafficClassTotalLastBytesXmit=_IbmfrBRSTrafficClassTotalLastBytesXmit_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,28),_IbmfrBRSTrafficClassTotalLastBytesXmit_Type())
ibmfrBRSTrafficClassTotalLastBytesXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassTotalLastBytesXmit.setStatus(_A)
_IbmfrBRSTrafficClassLastBytesXmitLow_Type=Counter32
_IbmfrBRSTrafficClassLastBytesXmitLow_Object=MibTableColumn
ibmfrBRSTrafficClassLastBytesXmitLow=_IbmfrBRSTrafficClassLastBytesXmitLow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,29),_IbmfrBRSTrafficClassLastBytesXmitLow_Type())
ibmfrBRSTrafficClassLastBytesXmitLow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastBytesXmitLow.setStatus(_A)
_IbmfrBRSTrafficClassLastBytesXmitNormal_Type=Counter32
_IbmfrBRSTrafficClassLastBytesXmitNormal_Object=MibTableColumn
ibmfrBRSTrafficClassLastBytesXmitNormal=_IbmfrBRSTrafficClassLastBytesXmitNormal_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,30),_IbmfrBRSTrafficClassLastBytesXmitNormal_Type())
ibmfrBRSTrafficClassLastBytesXmitNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastBytesXmitNormal.setStatus(_A)
_IbmfrBRSTrafficClassLastBytesXmitHigh_Type=Counter32
_IbmfrBRSTrafficClassLastBytesXmitHigh_Object=MibTableColumn
ibmfrBRSTrafficClassLastBytesXmitHigh=_IbmfrBRSTrafficClassLastBytesXmitHigh_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,31),_IbmfrBRSTrafficClassLastBytesXmitHigh_Type())
ibmfrBRSTrafficClassLastBytesXmitHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastBytesXmitHigh.setStatus(_A)
_IbmfrBRSTrafficClassLastBytesXmitUrgent_Type=Counter32
_IbmfrBRSTrafficClassLastBytesXmitUrgent_Object=MibTableColumn
ibmfrBRSTrafficClassLastBytesXmitUrgent=_IbmfrBRSTrafficClassLastBytesXmitUrgent_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,32),_IbmfrBRSTrafficClassLastBytesXmitUrgent_Type())
ibmfrBRSTrafficClassLastBytesXmitUrgent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastBytesXmitUrgent.setStatus(_A)
_IbmfrBRSTrafficClassTotalLastBytesOverflow_Type=Counter32
_IbmfrBRSTrafficClassTotalLastBytesOverflow_Object=MibTableColumn
ibmfrBRSTrafficClassTotalLastBytesOverflow=_IbmfrBRSTrafficClassTotalLastBytesOverflow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,33),_IbmfrBRSTrafficClassTotalLastBytesOverflow_Type())
ibmfrBRSTrafficClassTotalLastBytesOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassTotalLastBytesOverflow.setStatus(_A)
_IbmfrBRSTrafficClassLastBytesOverflowLow_Type=Counter32
_IbmfrBRSTrafficClassLastBytesOverflowLow_Object=MibTableColumn
ibmfrBRSTrafficClassLastBytesOverflowLow=_IbmfrBRSTrafficClassLastBytesOverflowLow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,34),_IbmfrBRSTrafficClassLastBytesOverflowLow_Type())
ibmfrBRSTrafficClassLastBytesOverflowLow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastBytesOverflowLow.setStatus(_A)
_IbmfrBRSTrafficClassLastBytesOverflowNmal_Type=Counter32
_IbmfrBRSTrafficClassLastBytesOverflowNmal_Object=MibTableColumn
ibmfrBRSTrafficClassLastBytesOverflowNmal=_IbmfrBRSTrafficClassLastBytesOverflowNmal_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,35),_IbmfrBRSTrafficClassLastBytesOverflowNmal_Type())
ibmfrBRSTrafficClassLastBytesOverflowNmal.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastBytesOverflowNmal.setStatus(_A)
_IbmfrBRSTrafficClassLastBytesOverflowHigh_Type=Counter32
_IbmfrBRSTrafficClassLastBytesOverflowHigh_Object=MibTableColumn
ibmfrBRSTrafficClassLastBytesOverflowHigh=_IbmfrBRSTrafficClassLastBytesOverflowHigh_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,36),_IbmfrBRSTrafficClassLastBytesOverflowHigh_Type())
ibmfrBRSTrafficClassLastBytesOverflowHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastBytesOverflowHigh.setStatus(_A)
_IbmfrBRSTrafficClassLastBytesOverflowUgent_Type=Counter32
_IbmfrBRSTrafficClassLastBytesOverflowUgent_Object=MibTableColumn
ibmfrBRSTrafficClassLastBytesOverflowUgent=_IbmfrBRSTrafficClassLastBytesOverflowUgent_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,37),_IbmfrBRSTrafficClassLastBytesOverflowUgent_Type())
ibmfrBRSTrafficClassLastBytesOverflowUgent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastBytesOverflowUgent.setStatus(_A)
_IbmfrBRSTrafficClassTotalLastPacketOverflow_Type=Counter32
_IbmfrBRSTrafficClassTotalLastPacketOverflow_Object=MibTableColumn
ibmfrBRSTrafficClassTotalLastPacketOverflow=_IbmfrBRSTrafficClassTotalLastPacketOverflow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,38),_IbmfrBRSTrafficClassTotalLastPacketOverflow_Type())
ibmfrBRSTrafficClassTotalLastPacketOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassTotalLastPacketOverflow.setStatus(_A)
_IbmfrBRSTrafficClassLastPacketOverflowLow_Type=Counter32
_IbmfrBRSTrafficClassLastPacketOverflowLow_Object=MibTableColumn
ibmfrBRSTrafficClassLastPacketOverflowLow=_IbmfrBRSTrafficClassLastPacketOverflowLow_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,39),_IbmfrBRSTrafficClassLastPacketOverflowLow_Type())
ibmfrBRSTrafficClassLastPacketOverflowLow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastPacketOverflowLow.setStatus(_A)
_IbmfrBRSTrafficClassLastPacketOverflowNmal_Type=Counter32
_IbmfrBRSTrafficClassLastPacketOverflowNmal_Object=MibTableColumn
ibmfrBRSTrafficClassLastPacketOverflowNmal=_IbmfrBRSTrafficClassLastPacketOverflowNmal_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,40),_IbmfrBRSTrafficClassLastPacketOverflowNmal_Type())
ibmfrBRSTrafficClassLastPacketOverflowNmal.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastPacketOverflowNmal.setStatus(_A)
_IbmfrBRSTrafficClassLastPacketOverflowHigh_Type=Counter32
_IbmfrBRSTrafficClassLastPacketOverflowHigh_Object=MibTableColumn
ibmfrBRSTrafficClassLastPacketOverflowHigh=_IbmfrBRSTrafficClassLastPacketOverflowHigh_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,41),_IbmfrBRSTrafficClassLastPacketOverflowHigh_Type())
ibmfrBRSTrafficClassLastPacketOverflowHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastPacketOverflowHigh.setStatus(_A)
_IbmfrBRSTrafficClassLastPacketOverflowUgent_Type=Counter32
_IbmfrBRSTrafficClassLastPacketOverflowUgent_Object=MibTableColumn
ibmfrBRSTrafficClassLastPacketOverflowUgent=_IbmfrBRSTrafficClassLastPacketOverflowUgent_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,42),_IbmfrBRSTrafficClassLastPacketOverflowUgent_Type())
ibmfrBRSTrafficClassLastPacketOverflowUgent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassLastPacketOverflowUgent.setStatus(_A)
class _IbmfrBRSTrafficClassClearCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_IbmfrBRSTrafficClassClearCounters_Type.__name__=_D
_IbmfrBRSTrafficClassClearCounters_Object=MibTableColumn
ibmfrBRSTrafficClassClearCounters=_IbmfrBRSTrafficClassClearCounters_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,43),_IbmfrBRSTrafficClassClearCounters_Type())
ibmfrBRSTrafficClassClearCounters.setMaxAccess(_O)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassClearCounters.setStatus(_A)
_IbmfrBRSTrafficClassSVCName_Type=DisplayString
_IbmfrBRSTrafficClassSVCName_Object=MibTableColumn
ibmfrBRSTrafficClassSVCName=_IbmfrBRSTrafficClassSVCName_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,4,1,44),_IbmfrBRSTrafficClassSVCName_Type())
ibmfrBRSTrafficClassSVCName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSTrafficClassSVCName.setStatus(_A)
_IbmfrBRSProtFiltTable_Object=MibTable
ibmfrBRSProtFiltTable=_IbmfrBRSProtFiltTable_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,5))
if mibBuilder.loadTexts:ibmfrBRSProtFiltTable.setStatus(_A)
_IbmfrBRSProtFiltEntry_Object=MibTableRow
ibmfrBRSProtFiltEntry=_IbmfrBRSProtFiltEntry_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,5,1))
ibmfrBRSProtFiltEntry.setIndexNames((0,_E,_F),(0,_C,_G),(0,_C,_I),(0,_C,_J),(0,_C,_R))
if mibBuilder.loadTexts:ibmfrBRSProtFiltEntry.setStatus(_A)
_IbmfrBRSProtFiltId_Type=DisplayString
_IbmfrBRSProtFiltId_Object=MibTableColumn
ibmfrBRSProtFiltId=_IbmfrBRSProtFiltId_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,5,1,1),_IbmfrBRSProtFiltId_Type())
ibmfrBRSProtFiltId.setMaxAccess(_H)
if mibBuilder.loadTexts:ibmfrBRSProtFiltId.setStatus(_A)
class _IbmfrBRSProtFiltPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),(_P,2),('high',3),(_Q,4)))
_IbmfrBRSProtFiltPrio_Type.__name__=_D
_IbmfrBRSProtFiltPrio_Object=MibTableColumn
ibmfrBRSProtFiltPrio=_IbmfrBRSProtFiltPrio_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,5,1,2),_IbmfrBRSProtFiltPrio_Type())
ibmfrBRSProtFiltPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSProtFiltPrio.setStatus(_A)
class _IbmfrBRSProtFiltDE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_IbmfrBRSProtFiltDE_Type.__name__=_D
_IbmfrBRSProtFiltDE_Object=MibTableColumn
ibmfrBRSProtFiltDE=_IbmfrBRSProtFiltDE_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,5,1,3),_IbmfrBRSProtFiltDE_Type())
ibmfrBRSProtFiltDE.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSProtFiltDE.setStatus(_A)
_IbmfrBRSProtFiltSVCName_Type=DisplayString
_IbmfrBRSProtFiltSVCName_Object=MibTableColumn
ibmfrBRSProtFiltSVCName=_IbmfrBRSProtFiltSVCName_Object((1,3,6,1,4,1,2,6,119,4,4,4,1,5,1,4),_IbmfrBRSProtFiltSVCName_Type())
ibmfrBRSProtFiltSVCName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmfrBRSProtFiltSVCName.setStatus(_A)
_IbmfrBRSAdministravive_ObjectIdentity=ObjectIdentity
ibmfrBRSAdministravive=_IbmfrBRSAdministravive_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,4,4,2))
mibBuilder.exportSymbols(_C,**{'ibmfrBRS':ibmfrBRS,'ibmfrBRSOperational':ibmfrBRSOperational,'ibmfrBRSInterfaceTable':ibmfrBRSInterfaceTable,'ibmfrBRSInterfaceEntry':ibmfrBRSInterfaceEntry,'ibmfrBRSInterfaceMaxQueue':ibmfrBRSInterfaceMaxQueue,'ibmfrBRSInterfaceMinQueue':ibmfrBRSInterfaceMinQueue,'ibmfrBRSInterfaceTotalBandwidth':ibmfrBRSInterfaceTotalBandwidth,'ibmfrBRSInterfaceTotalCircuitClasses':ibmfrBRSInterfaceTotalCircuitClasses,'ibmfrBRSInterfaceDefaultCircuitClassName':ibmfrBRSInterfaceDefaultCircuitClassName,'ibmfrBRSCircuitClassTable':ibmfrBRSCircuitClassTable,'ibmfrBRSCircuitClassEntry':ibmfrBRSCircuitClassEntry,_G:ibmfrBRSCircuitClassName,'ibmfrBRSCircuitClassBandwidth':ibmfrBRSCircuitClassBandwidth,'ibmfrBRSCircuitClassPacketXmit':ibmfrBRSCircuitClassPacketXmit,'ibmfrBRSCircuitClassBytesXmit':ibmfrBRSCircuitClassBytesXmit,'ibmfrBRSCircuitClassBytesOverflow':ibmfrBRSCircuitClassBytesOverflow,'ibmfrBRSCircuitClassLastPacketXmit':ibmfrBRSCircuitClassLastPacketXmit,'ibmfrBRSCircuitClassLastBytesXmit':ibmfrBRSCircuitClassLastBytesXmit,'ibmfrBRSCircuitClassLastBytesOverflow':ibmfrBRSCircuitClassLastBytesOverflow,'ibmfrBRSCircuitClassClearCounters':ibmfrBRSCircuitClassClearCounters,'ibmfrBRSCircuitTable':ibmfrBRSCircuitTable,'ibmfrBRSCircuitEntry':ibmfrBRSCircuitEntry,_I:ibmfrBRSCircuitNumber,'ibmfrBRSCircuitMaxQueue':ibmfrBRSCircuitMaxQueue,'ibmfrBRSCircuitMinQueue':ibmfrBRSCircuitMinQueue,'ibmfrBRSCircuitTotalBandwidth':ibmfrBRSCircuitTotalBandwidth,'ibmfrBRSCircuitTotalTrafficClasses':ibmfrBRSCircuitTotalTrafficClasses,'ibmfrBRSCircuitDefaultTrafficClassName':ibmfrBRSCircuitDefaultTrafficClassName,'ibmfrBRSCircuitDefaultTrafficClassPrio':ibmfrBRSCircuitDefaultTrafficClassPrio,'ibmfrBRSCircuitSpecification':ibmfrBRSCircuitSpecification,'ibmfrBRSCircuitSuperClassName':ibmfrBRSCircuitSuperClassName,'ibmfrBRSCircuitSVCName':ibmfrBRSCircuitSVCName,'ibmfrBRSTrafficClassTable':ibmfrBRSTrafficClassTable,'ibmfrBRSTrafficClassEntry':ibmfrBRSTrafficClassEntry,_J:ibmfrBRSTrafficClassName,'ibmfrBRSTrafficClassBandwidth':ibmfrBRSTrafficClassBandwidth,'ibmfrBRSTrafficClassTotalPacketXmit':ibmfrBRSTrafficClassTotalPacketXmit,'ibmfrBRSTrafficClassPacketXmitLow':ibmfrBRSTrafficClassPacketXmitLow,'ibmfrBRSTrafficClassPacketXmitNormal':ibmfrBRSTrafficClassPacketXmitNormal,'ibmfrBRSTrafficClassPacketXmitHigh':ibmfrBRSTrafficClassPacketXmitHigh,'ibmfrBRSTrafficClassPacketXmitUrgent':ibmfrBRSTrafficClassPacketXmitUrgent,'ibmfrBRSTrafficClassTotalBytesXmit':ibmfrBRSTrafficClassTotalBytesXmit,'ibmfrBRSTrafficClassBytesXmitLow':ibmfrBRSTrafficClassBytesXmitLow,'ibmfrBRSTrafficClassBytesXmitNormal':ibmfrBRSTrafficClassBytesXmitNormal,'ibmfrBRSTrafficClassBytesXmitHigh':ibmfrBRSTrafficClassBytesXmitHigh,'ibmfrBRSTrafficClassBytesXmitUrgent':ibmfrBRSTrafficClassBytesXmitUrgent,'ibmfrBRSTrafficClassTotalBytesOverflow':ibmfrBRSTrafficClassTotalBytesOverflow,'ibmfrBRSTrafficClassBytesOverflowLow':ibmfrBRSTrafficClassBytesOverflowLow,'ibmfrBRSTrafficClassBytesOverflowNormal':ibmfrBRSTrafficClassBytesOverflowNormal,'ibmfrBRSTrafficClassBytesOverflowHigh':ibmfrBRSTrafficClassBytesOverflowHigh,'ibmfrBRSTrafficClassBytesOverflowUrgent':ibmfrBRSTrafficClassBytesOverflowUrgent,'ibmfrBRSTrafficClassTotalPacketOverflow':ibmfrBRSTrafficClassTotalPacketOverflow,'ibmfrBRSTrafficClassPacketOverflowLow':ibmfrBRSTrafficClassPacketOverflowLow,'ibmfrBRSTrafficClassPacketOverflowNormal':ibmfrBRSTrafficClassPacketOverflowNormal,'ibmfrBRSTrafficClassPacketOverflowHigh':ibmfrBRSTrafficClassPacketOverflowHigh,'ibmfrBRSTrafficClassPacketOverflowUrgent':ibmfrBRSTrafficClassPacketOverflowUrgent,'ibmfrBRSTrafficClassTotalLastPacketXmit':ibmfrBRSTrafficClassTotalLastPacketXmit,'ibmfrBRSTrafficClassLastPacketXmitLow':ibmfrBRSTrafficClassLastPacketXmitLow,'ibmfrBRSTrafficClassLastPacketXmitNormal':ibmfrBRSTrafficClassLastPacketXmitNormal,'ibmfrBRSTrafficClassLastPacketXmitHigh':ibmfrBRSTrafficClassLastPacketXmitHigh,'ibmfrBRSTrafficClassLastPacketXmitUrgent':ibmfrBRSTrafficClassLastPacketXmitUrgent,'ibmfrBRSTrafficClassTotalLastBytesXmit':ibmfrBRSTrafficClassTotalLastBytesXmit,'ibmfrBRSTrafficClassLastBytesXmitLow':ibmfrBRSTrafficClassLastBytesXmitLow,'ibmfrBRSTrafficClassLastBytesXmitNormal':ibmfrBRSTrafficClassLastBytesXmitNormal,'ibmfrBRSTrafficClassLastBytesXmitHigh':ibmfrBRSTrafficClassLastBytesXmitHigh,'ibmfrBRSTrafficClassLastBytesXmitUrgent':ibmfrBRSTrafficClassLastBytesXmitUrgent,'ibmfrBRSTrafficClassTotalLastBytesOverflow':ibmfrBRSTrafficClassTotalLastBytesOverflow,'ibmfrBRSTrafficClassLastBytesOverflowLow':ibmfrBRSTrafficClassLastBytesOverflowLow,'ibmfrBRSTrafficClassLastBytesOverflowNmal':ibmfrBRSTrafficClassLastBytesOverflowNmal,'ibmfrBRSTrafficClassLastBytesOverflowHigh':ibmfrBRSTrafficClassLastBytesOverflowHigh,'ibmfrBRSTrafficClassLastBytesOverflowUgent':ibmfrBRSTrafficClassLastBytesOverflowUgent,'ibmfrBRSTrafficClassTotalLastPacketOverflow':ibmfrBRSTrafficClassTotalLastPacketOverflow,'ibmfrBRSTrafficClassLastPacketOverflowLow':ibmfrBRSTrafficClassLastPacketOverflowLow,'ibmfrBRSTrafficClassLastPacketOverflowNmal':ibmfrBRSTrafficClassLastPacketOverflowNmal,'ibmfrBRSTrafficClassLastPacketOverflowHigh':ibmfrBRSTrafficClassLastPacketOverflowHigh,'ibmfrBRSTrafficClassLastPacketOverflowUgent':ibmfrBRSTrafficClassLastPacketOverflowUgent,'ibmfrBRSTrafficClassClearCounters':ibmfrBRSTrafficClassClearCounters,'ibmfrBRSTrafficClassSVCName':ibmfrBRSTrafficClassSVCName,'ibmfrBRSProtFiltTable':ibmfrBRSProtFiltTable,'ibmfrBRSProtFiltEntry':ibmfrBRSProtFiltEntry,_R:ibmfrBRSProtFiltId,'ibmfrBRSProtFiltPrio':ibmfrBRSProtFiltPrio,'ibmfrBRSProtFiltDE':ibmfrBRSProtFiltDE,'ibmfrBRSProtFiltSVCName':ibmfrBRSProtFiltSVCName,'ibmfrBRSAdministravive':ibmfrBRSAdministravive})