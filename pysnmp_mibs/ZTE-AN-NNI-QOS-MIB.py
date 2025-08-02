_N='zxAnNniQosConformDscpDscp'
_M='disable'
_L='enable'
_K='not-accessible'
_J='zxAnNniQosShapeConfDir'
_I='ZTE-AN-NNI-QOS-MIB'
_H='out'
_G='read-write'
_F='OctetString'
_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnNniQosMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,22))
_ZxAnNniQosObjects_ObjectIdentity=ObjectIdentity
zxAnNniQosObjects=_ZxAnNniQosObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,22,1))
_ZxAnNniQosGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnNniQosGlobalObjects=_ZxAnNniQosGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,22,1,1))
class _ZxAnNniQosCos2Queue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnNniQosCos2Queue_Type.__name__=_F
_ZxAnNniQosCos2Queue_Object=MibScalar
zxAnNniQosCos2Queue=_ZxAnNniQosCos2Queue_Object((1,3,6,1,4,1,3902,1015,22,1,1,1),_ZxAnNniQosCos2Queue_Type())
zxAnNniQosCos2Queue.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnNniQosCos2Queue.setStatus(_A)
class _ZxAnNniQosCos2Drop_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnNniQosCos2Drop_Type.__name__=_F
_ZxAnNniQosCos2Drop_Object=MibScalar
zxAnNniQosCos2Drop=_ZxAnNniQosCos2Drop_Object((1,3,6,1,4,1,3902,1015,22,1,1,8),_ZxAnNniQosCos2Drop_Type())
zxAnNniQosCos2Drop.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnNniQosCos2Drop.setStatus(_A)
class _ZxAnNniQosTrustMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('untrust',1),('trustcosonly',2),('trustdscponly',3),('notsupport',255)))
_ZxAnNniQosTrustMode_Type.__name__=_C
_ZxAnNniQosTrustMode_Object=MibScalar
zxAnNniQosTrustMode=_ZxAnNniQosTrustMode_Object((1,3,6,1,4,1,3902,1015,22,1,1,9),_ZxAnNniQosTrustMode_Type())
zxAnNniQosTrustMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnNniQosTrustMode.setStatus(_A)
_ZxAnNniQosQueueSchedTable_Object=MibTable
zxAnNniQosQueueSchedTable=_ZxAnNniQosQueueSchedTable_Object((1,3,6,1,4,1,3902,1015,22,1,2))
if mibBuilder.loadTexts:zxAnNniQosQueueSchedTable.setStatus(_A)
_ZxAnNniQosQueueSchedEntry_Object=MibTableRow
zxAnNniQosQueueSchedEntry=_ZxAnNniQosQueueSchedEntry_Object((1,3,6,1,4,1,3902,1015,22,1,2,1))
zxAnNniQosQueueSchedEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnNniQosQueueSchedEntry.setStatus(_A)
class _ZxAnNniQosQueueSchedAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sp',1),('wrr',2),('fq',3)))
_ZxAnNniQosQueueSchedAlgorithm_Type.__name__=_C
_ZxAnNniQosQueueSchedAlgorithm_Object=MibTableColumn
zxAnNniQosQueueSchedAlgorithm=_ZxAnNniQosQueueSchedAlgorithm_Object((1,3,6,1,4,1,3902,1015,22,1,2,1,1),_ZxAnNniQosQueueSchedAlgorithm_Type())
zxAnNniQosQueueSchedAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosQueueSchedAlgorithm.setStatus(_A)
class _ZxAnNniQosQueueSchedWeight_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnNniQosQueueSchedWeight_Type.__name__=_F
_ZxAnNniQosQueueSchedWeight_Object=MibTableColumn
zxAnNniQosQueueSchedWeight=_ZxAnNniQosQueueSchedWeight_Object((1,3,6,1,4,1,3902,1015,22,1,2,1,2),_ZxAnNniQosQueueSchedWeight_Type())
zxAnNniQosQueueSchedWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosQueueSchedWeight.setStatus(_A)
_ZxAnNniQosQueueSchedMinRate_Type=ObjectIdentifier
_ZxAnNniQosQueueSchedMinRate_Object=MibTableColumn
zxAnNniQosQueueSchedMinRate=_ZxAnNniQosQueueSchedMinRate_Object((1,3,6,1,4,1,3902,1015,22,1,2,1,3),_ZxAnNniQosQueueSchedMinRate_Type())
zxAnNniQosQueueSchedMinRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosQueueSchedMinRate.setStatus(_A)
_ZxAnNniQosQueueSchedMaxRate_Type=ObjectIdentifier
_ZxAnNniQosQueueSchedMaxRate_Object=MibTableColumn
zxAnNniQosQueueSchedMaxRate=_ZxAnNniQosQueueSchedMaxRate_Object((1,3,6,1,4,1,3902,1015,22,1,2,1,4),_ZxAnNniQosQueueSchedMaxRate_Type())
zxAnNniQosQueueSchedMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosQueueSchedMaxRate.setStatus(_A)
_ZxAnNniQosQueueSchedRowStatus_Type=RowStatus
_ZxAnNniQosQueueSchedRowStatus_Object=MibTableColumn
zxAnNniQosQueueSchedRowStatus=_ZxAnNniQosQueueSchedRowStatus_Object((1,3,6,1,4,1,3902,1015,22,1,2,1,10),_ZxAnNniQosQueueSchedRowStatus_Type())
zxAnNniQosQueueSchedRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosQueueSchedRowStatus.setStatus(_A)
_ZxAnNniQosAclBindTable_Object=MibTable
zxAnNniQosAclBindTable=_ZxAnNniQosAclBindTable_Object((1,3,6,1,4,1,3902,1015,22,1,3))
if mibBuilder.loadTexts:zxAnNniQosAclBindTable.setStatus(_A)
_ZxAnNniQosAclBindEntry_Object=MibTableRow
zxAnNniQosAclBindEntry=_ZxAnNniQosAclBindEntry_Object((1,3,6,1,4,1,3902,1015,22,1,3,1))
zxAnNniQosAclBindEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnNniQosAclBindEntry.setStatus(_A)
class _ZxAnNniQosAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,349))
_ZxAnNniQosAclIndex_Type.__name__=_C
_ZxAnNniQosAclIndex_Object=MibTableColumn
zxAnNniQosAclIndex=_ZxAnNniQosAclIndex_Object((1,3,6,1,4,1,3902,1015,22,1,3,1,1),_ZxAnNniQosAclIndex_Type())
zxAnNniQosAclIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosAclIndex.setStatus(_A)
class _ZxAnNniQosAclBindDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),(_H,2)))
_ZxAnNniQosAclBindDir_Type.__name__=_C
_ZxAnNniQosAclBindDir_Object=MibTableColumn
zxAnNniQosAclBindDir=_ZxAnNniQosAclBindDir_Object((1,3,6,1,4,1,3902,1015,22,1,3,1,2),_ZxAnNniQosAclBindDir_Type())
zxAnNniQosAclBindDir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosAclBindDir.setStatus(_A)
_ZxAnNniQosAclBindRowStatus_Type=RowStatus
_ZxAnNniQosAclBindRowStatus_Object=MibTableColumn
zxAnNniQosAclBindRowStatus=_ZxAnNniQosAclBindRowStatus_Object((1,3,6,1,4,1,3902,1015,22,1,3,1,10),_ZxAnNniQosAclBindRowStatus_Type())
zxAnNniQosAclBindRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosAclBindRowStatus.setStatus(_A)
_ZxAnNniQosShapeTable_Object=MibTable
zxAnNniQosShapeTable=_ZxAnNniQosShapeTable_Object((1,3,6,1,4,1,3902,1015,22,1,4))
if mibBuilder.loadTexts:zxAnNniQosShapeTable.setStatus(_A)
_ZxAnNniQosShapeEntry_Object=MibTableRow
zxAnNniQosShapeEntry=_ZxAnNniQosShapeEntry_Object((1,3,6,1,4,1,3902,1015,22,1,4,1))
zxAnNniQosShapeEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnNniQosShapeEntry.setStatus(_A)
_ZxAnNniQosShapeRate_Type=Integer32
_ZxAnNniQosShapeRate_Object=MibTableColumn
zxAnNniQosShapeRate=_ZxAnNniQosShapeRate_Object((1,3,6,1,4,1,3902,1015,22,1,4,1,1),_ZxAnNniQosShapeRate_Type())
zxAnNniQosShapeRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosShapeRate.setStatus(_A)
_ZxAnNniQosShapeBurstSize_Type=Integer32
_ZxAnNniQosShapeBurstSize_Object=MibTableColumn
zxAnNniQosShapeBurstSize=_ZxAnNniQosShapeBurstSize_Object((1,3,6,1,4,1,3902,1015,22,1,4,1,2),_ZxAnNniQosShapeBurstSize_Type())
zxAnNniQosShapeBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosShapeBurstSize.setStatus(_A)
class _ZxAnNniQosShapeDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),(_H,2)))
_ZxAnNniQosShapeDir_Type.__name__=_C
_ZxAnNniQosShapeDir_Object=MibTableColumn
zxAnNniQosShapeDir=_ZxAnNniQosShapeDir_Object((1,3,6,1,4,1,3902,1015,22,1,4,1,3),_ZxAnNniQosShapeDir_Type())
zxAnNniQosShapeDir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosShapeDir.setStatus(_A)
_ZxAnNniQosShapeRowStatus_Type=RowStatus
_ZxAnNniQosShapeRowStatus_Object=MibTableColumn
zxAnNniQosShapeRowStatus=_ZxAnNniQosShapeRowStatus_Object((1,3,6,1,4,1,3902,1015,22,1,4,1,10),_ZxAnNniQosShapeRowStatus_Type())
zxAnNniQosShapeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosShapeRowStatus.setStatus(_A)
_ZxAnNniQosShapeConfTable_Object=MibTable
zxAnNniQosShapeConfTable=_ZxAnNniQosShapeConfTable_Object((1,3,6,1,4,1,3902,1015,22,1,5))
if mibBuilder.loadTexts:zxAnNniQosShapeConfTable.setStatus(_A)
_ZxAnNniQosShapeConfEntry_Object=MibTableRow
zxAnNniQosShapeConfEntry=_ZxAnNniQosShapeConfEntry_Object((1,3,6,1,4,1,3902,1015,22,1,5,1))
zxAnNniQosShapeConfEntry.setIndexNames((0,_D,_E),(0,_I,_J))
if mibBuilder.loadTexts:zxAnNniQosShapeConfEntry.setStatus(_A)
class _ZxAnNniQosShapeConfDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),(_H,2)))
_ZxAnNniQosShapeConfDir_Type.__name__=_C
_ZxAnNniQosShapeConfDir_Object=MibTableColumn
zxAnNniQosShapeConfDir=_ZxAnNniQosShapeConfDir_Object((1,3,6,1,4,1,3902,1015,22,1,5,1,1),_ZxAnNniQosShapeConfDir_Type())
zxAnNniQosShapeConfDir.setMaxAccess(_K)
if mibBuilder.loadTexts:zxAnNniQosShapeConfDir.setStatus(_A)
_ZxAnNniQosShapeConfRate_Type=Integer32
_ZxAnNniQosShapeConfRate_Object=MibTableColumn
zxAnNniQosShapeConfRate=_ZxAnNniQosShapeConfRate_Object((1,3,6,1,4,1,3902,1015,22,1,5,1,2),_ZxAnNniQosShapeConfRate_Type())
zxAnNniQosShapeConfRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosShapeConfRate.setStatus(_A)
_ZxAnNniQosShapeConfBurstSize_Type=Integer32
_ZxAnNniQosShapeConfBurstSize_Object=MibTableColumn
zxAnNniQosShapeConfBurstSize=_ZxAnNniQosShapeConfBurstSize_Object((1,3,6,1,4,1,3902,1015,22,1,5,1,3),_ZxAnNniQosShapeConfBurstSize_Type())
zxAnNniQosShapeConfBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosShapeConfBurstSize.setStatus(_A)
_ZxAnNniQosShapeConfRowStatus_Type=RowStatus
_ZxAnNniQosShapeConfRowStatus_Object=MibTableColumn
zxAnNniQosShapeConfRowStatus=_ZxAnNniQosShapeConfRowStatus_Object((1,3,6,1,4,1,3902,1015,22,1,5,1,10),_ZxAnNniQosShapeConfRowStatus_Type())
zxAnNniQosShapeConfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosShapeConfRowStatus.setStatus(_A)
_ZxAnNniQosTrustTable_Object=MibTable
zxAnNniQosTrustTable=_ZxAnNniQosTrustTable_Object((1,3,6,1,4,1,3902,1015,22,1,6))
if mibBuilder.loadTexts:zxAnNniQosTrustTable.setStatus(_A)
_ZxAnNniQosTrustEntry_Object=MibTableRow
zxAnNniQosTrustEntry=_ZxAnNniQosTrustEntry_Object((1,3,6,1,4,1,3902,1015,22,1,6,1))
zxAnNniQosTrustEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnNniQosTrustEntry.setStatus(_A)
class _ZxAnNniQosTrustDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_ZxAnNniQosTrustDscp_Type.__name__=_C
_ZxAnNniQosTrustDscp_Object=MibTableColumn
zxAnNniQosTrustDscp=_ZxAnNniQosTrustDscp_Object((1,3,6,1,4,1,3902,1015,22,1,6,1,1),_ZxAnNniQosTrustDscp_Type())
zxAnNniQosTrustDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosTrustDscp.setStatus(_A)
class _ZxAnNniQosTrustCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_ZxAnNniQosTrustCos_Type.__name__=_C
_ZxAnNniQosTrustCos_Object=MibTableColumn
zxAnNniQosTrustCos=_ZxAnNniQosTrustCos_Object((1,3,6,1,4,1,3902,1015,22,1,6,1,2),_ZxAnNniQosTrustCos_Type())
zxAnNniQosTrustCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosTrustCos.setStatus(_A)
_ZxAnNniQosConformDscpTable_Object=MibTable
zxAnNniQosConformDscpTable=_ZxAnNniQosConformDscpTable_Object((1,3,6,1,4,1,3902,1015,22,1,7))
if mibBuilder.loadTexts:zxAnNniQosConformDscpTable.setStatus(_A)
_ZxAnNniQosConformDscpEntry_Object=MibTableRow
zxAnNniQosConformDscpEntry=_ZxAnNniQosConformDscpEntry_Object((1,3,6,1,4,1,3902,1015,22,1,7,1))
zxAnNniQosConformDscpEntry.setIndexNames((0,_I,_N))
if mibBuilder.loadTexts:zxAnNniQosConformDscpEntry.setStatus(_A)
class _ZxAnNniQosConformDscpDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ZxAnNniQosConformDscpDscp_Type.__name__=_C
_ZxAnNniQosConformDscpDscp_Object=MibTableColumn
zxAnNniQosConformDscpDscp=_ZxAnNniQosConformDscpDscp_Object((1,3,6,1,4,1,3902,1015,22,1,7,1,1),_ZxAnNniQosConformDscpDscp_Type())
zxAnNniQosConformDscpDscp.setMaxAccess(_K)
if mibBuilder.loadTexts:zxAnNniQosConformDscpDscp.setStatus(_A)
class _ZxAnNniQosConformDscpNewDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ZxAnNniQosConformDscpNewDscp_Type.__name__=_C
_ZxAnNniQosConformDscpNewDscp_Object=MibTableColumn
zxAnNniQosConformDscpNewDscp=_ZxAnNniQosConformDscpNewDscp_Object((1,3,6,1,4,1,3902,1015,22,1,7,1,2),_ZxAnNniQosConformDscpNewDscp_Type())
zxAnNniQosConformDscpNewDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosConformDscpNewDscp.setStatus(_A)
class _ZxAnNniQosConformDscpNewCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnNniQosConformDscpNewCos_Type.__name__=_C
_ZxAnNniQosConformDscpNewCos_Object=MibTableColumn
zxAnNniQosConformDscpNewCos=_ZxAnNniQosConformDscpNewCos_Object((1,3,6,1,4,1,3902,1015,22,1,7,1,3),_ZxAnNniQosConformDscpNewCos_Type())
zxAnNniQosConformDscpNewCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosConformDscpNewCos.setStatus(_A)
class _ZxAnNniQosConformDscpNewDp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_ZxAnNniQosConformDscpNewDp_Type.__name__=_C
_ZxAnNniQosConformDscpNewDp_Object=MibTableColumn
zxAnNniQosConformDscpNewDp=_ZxAnNniQosConformDscpNewDp_Object((1,3,6,1,4,1,3902,1015,22,1,7,1,4),_ZxAnNniQosConformDscpNewDp_Type())
zxAnNniQosConformDscpNewDp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosConformDscpNewDp.setStatus(_A)
_ZxAnNniQosConformDscpRowStatus_Type=RowStatus
_ZxAnNniQosConformDscpRowStatus_Object=MibTableColumn
zxAnNniQosConformDscpRowStatus=_ZxAnNniQosConformDscpRowStatus_Object((1,3,6,1,4,1,3902,1015,22,1,7,1,10),_ZxAnNniQosConformDscpRowStatus_Type())
zxAnNniQosConformDscpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnNniQosConformDscpRowStatus.setStatus(_A)
_ZxAnNniQosTrapObjects_ObjectIdentity=ObjectIdentity
zxAnNniQosTrapObjects=_ZxAnNniQosTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,22,2))
mibBuilder.exportSymbols(_I,**{'zxAnNniQosMib':zxAnNniQosMib,'zxAnNniQosObjects':zxAnNniQosObjects,'zxAnNniQosGlobalObjects':zxAnNniQosGlobalObjects,'zxAnNniQosCos2Queue':zxAnNniQosCos2Queue,'zxAnNniQosCos2Drop':zxAnNniQosCos2Drop,'zxAnNniQosTrustMode':zxAnNniQosTrustMode,'zxAnNniQosQueueSchedTable':zxAnNniQosQueueSchedTable,'zxAnNniQosQueueSchedEntry':zxAnNniQosQueueSchedEntry,'zxAnNniQosQueueSchedAlgorithm':zxAnNniQosQueueSchedAlgorithm,'zxAnNniQosQueueSchedWeight':zxAnNniQosQueueSchedWeight,'zxAnNniQosQueueSchedMinRate':zxAnNniQosQueueSchedMinRate,'zxAnNniQosQueueSchedMaxRate':zxAnNniQosQueueSchedMaxRate,'zxAnNniQosQueueSchedRowStatus':zxAnNniQosQueueSchedRowStatus,'zxAnNniQosAclBindTable':zxAnNniQosAclBindTable,'zxAnNniQosAclBindEntry':zxAnNniQosAclBindEntry,'zxAnNniQosAclIndex':zxAnNniQosAclIndex,'zxAnNniQosAclBindDir':zxAnNniQosAclBindDir,'zxAnNniQosAclBindRowStatus':zxAnNniQosAclBindRowStatus,'zxAnNniQosShapeTable':zxAnNniQosShapeTable,'zxAnNniQosShapeEntry':zxAnNniQosShapeEntry,'zxAnNniQosShapeRate':zxAnNniQosShapeRate,'zxAnNniQosShapeBurstSize':zxAnNniQosShapeBurstSize,'zxAnNniQosShapeDir':zxAnNniQosShapeDir,'zxAnNniQosShapeRowStatus':zxAnNniQosShapeRowStatus,'zxAnNniQosShapeConfTable':zxAnNniQosShapeConfTable,'zxAnNniQosShapeConfEntry':zxAnNniQosShapeConfEntry,_J:zxAnNniQosShapeConfDir,'zxAnNniQosShapeConfRate':zxAnNniQosShapeConfRate,'zxAnNniQosShapeConfBurstSize':zxAnNniQosShapeConfBurstSize,'zxAnNniQosShapeConfRowStatus':zxAnNniQosShapeConfRowStatus,'zxAnNniQosTrustTable':zxAnNniQosTrustTable,'zxAnNniQosTrustEntry':zxAnNniQosTrustEntry,'zxAnNniQosTrustDscp':zxAnNniQosTrustDscp,'zxAnNniQosTrustCos':zxAnNniQosTrustCos,'zxAnNniQosConformDscpTable':zxAnNniQosConformDscpTable,'zxAnNniQosConformDscpEntry':zxAnNniQosConformDscpEntry,_N:zxAnNniQosConformDscpDscp,'zxAnNniQosConformDscpNewDscp':zxAnNniQosConformDscpNewDscp,'zxAnNniQosConformDscpNewCos':zxAnNniQosConformDscpNewCos,'zxAnNniQosConformDscpNewDp':zxAnNniQosConformDscpNewDp,'zxAnNniQosConformDscpRowStatus':zxAnNniQosConformDscpRowStatus,'zxAnNniQosTrapObjects':zxAnNniQosTrapObjects})