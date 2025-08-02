_k='ciscoBusSubIfGroup'
_j='ciscoBusGroup'
_i='busClientAtmAddress'
_h='busClientMSendVci'
_g='busClientMSendVpi'
_f='busClientIfIndex'
_e='busSubIfNum'
_d='busStatus'
_c='busAdminStatus'
_b='busOperStatus'
_a='busMultiFwdVci'
_Z='busMultiFwdVpi'
_Y='busFrmTimeOuts'
_X='busOutFwdNUcastFrms'
_W='busOutFwdUcastFrms'
_V='busOutFwdOctets'
_U='busMaxFrmAge'
_T='busMaxFrm'
_S='busLanType'
_R='busUpTime'
_Q='busIfIndex'
_P='busAtmAddrActl'
_O='busAtmAddrMask'
_N='busAtmAddrSpec'
_M='busClientId'
_L='inactive'
_K='active'
_J='DisplayString'
_I='OctetString'
_H='not-accessible'
_G='busIndex'
_F='busElanName'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='CISCO-BUS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
AtmLaneAddress,=mibBuilder.importSymbols('LAN-EMULATION-CLIENT-MIB','AtmLaneAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention','TimeStamp')
ciscoBusMIB=ModuleIdentity((1,3,6,1,4,1,9,9,40))
class CiscoVpiInteger(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
class CiscoVciInteger(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_CiscoBusMIBObjects_ObjectIdentity=ObjectIdentity
ciscoBusMIBObjects=_CiscoBusMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,40,1))
_BusTable_Object=MibTable
busTable=_BusTable_Object((1,3,6,1,4,1,9,9,40,1,1))
if mibBuilder.loadTexts:busTable.setStatus(_A)
_BusEntry_Object=MibTableRow
busEntry=_BusEntry_Object((1,3,6,1,4,1,9,9,40,1,1,1))
busEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:busEntry.setStatus(_A)
class _BusElanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BusElanName_Type.__name__=_J
_BusElanName_Object=MibTableColumn
busElanName=_BusElanName_Object((1,3,6,1,4,1,9,9,40,1,1,1,1),_BusElanName_Type())
busElanName.setMaxAccess(_H)
if mibBuilder.loadTexts:busElanName.setStatus(_A)
class _BusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BusIndex_Type.__name__=_E
_BusIndex_Object=MibTableColumn
busIndex=_BusIndex_Object((1,3,6,1,4,1,9,9,40,1,1,1,2),_BusIndex_Type())
busIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:busIndex.setStatus(_A)
_BusAtmAddrSpec_Type=AtmLaneAddress
_BusAtmAddrSpec_Object=MibTableColumn
busAtmAddrSpec=_BusAtmAddrSpec_Object((1,3,6,1,4,1,9,9,40,1,1,1,3),_BusAtmAddrSpec_Type())
busAtmAddrSpec.setMaxAccess(_D)
if mibBuilder.loadTexts:busAtmAddrSpec.setStatus(_A)
class _BusAtmAddrMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(20,20))
_BusAtmAddrMask_Type.__name__=_I
_BusAtmAddrMask_Object=MibTableColumn
busAtmAddrMask=_BusAtmAddrMask_Object((1,3,6,1,4,1,9,9,40,1,1,1,4),_BusAtmAddrMask_Type())
busAtmAddrMask.setMaxAccess(_D)
if mibBuilder.loadTexts:busAtmAddrMask.setStatus(_A)
_BusAtmAddrActl_Type=AtmLaneAddress
_BusAtmAddrActl_Object=MibTableColumn
busAtmAddrActl=_BusAtmAddrActl_Object((1,3,6,1,4,1,9,9,40,1,1,1,5),_BusAtmAddrActl_Type())
busAtmAddrActl.setMaxAccess(_C)
if mibBuilder.loadTexts:busAtmAddrActl.setStatus(_A)
_BusIfIndex_Type=Integer32
_BusIfIndex_Object=MibTableColumn
busIfIndex=_BusIfIndex_Object((1,3,6,1,4,1,9,9,40,1,1,1,6),_BusIfIndex_Type())
busIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:busIfIndex.setStatus(_A)
_BusSubIfNum_Type=Integer32
_BusSubIfNum_Object=MibTableColumn
busSubIfNum=_BusSubIfNum_Object((1,3,6,1,4,1,9,9,40,1,1,1,7),_BusSubIfNum_Type())
busSubIfNum.setMaxAccess(_D)
if mibBuilder.loadTexts:busSubIfNum.setStatus(_A)
_BusUpTime_Type=TimeStamp
_BusUpTime_Object=MibTableColumn
busUpTime=_BusUpTime_Object((1,3,6,1,4,1,9,9,40,1,1,1,8),_BusUpTime_Type())
busUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:busUpTime.setStatus(_A)
class _BusLanType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot3',1),('dot5',2)))
_BusLanType_Type.__name__=_E
_BusLanType_Object=MibTableColumn
busLanType=_BusLanType_Object((1,3,6,1,4,1,9,9,40,1,1,1,9),_BusLanType_Type())
busLanType.setMaxAccess(_D)
if mibBuilder.loadTexts:busLanType.setStatus(_A)
class _BusMaxFrm_Type(Integer32):defaultValue=1516;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1516,4544,9234,18190)));namedValues=NamedValues(*(('dot3',1516),('tr4Mb',4544),('rfc1626',9234),('tr16Mb',18190)))
_BusMaxFrm_Type.__name__=_E
_BusMaxFrm_Object=MibTableColumn
busMaxFrm=_BusMaxFrm_Object((1,3,6,1,4,1,9,9,40,1,1,1,10),_BusMaxFrm_Type())
busMaxFrm.setMaxAccess(_D)
if mibBuilder.loadTexts:busMaxFrm.setStatus(_A)
class _BusMaxFrmAge_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BusMaxFrmAge_Type.__name__=_E
_BusMaxFrmAge_Object=MibTableColumn
busMaxFrmAge=_BusMaxFrmAge_Object((1,3,6,1,4,1,9,9,40,1,1,1,11),_BusMaxFrmAge_Type())
busMaxFrmAge.setMaxAccess(_D)
if mibBuilder.loadTexts:busMaxFrmAge.setStatus(_A)
if mibBuilder.loadTexts:busMaxFrmAge.setUnits('seconds')
_BusOutFwdOctets_Type=Counter32
_BusOutFwdOctets_Object=MibTableColumn
busOutFwdOctets=_BusOutFwdOctets_Object((1,3,6,1,4,1,9,9,40,1,1,1,12),_BusOutFwdOctets_Type())
busOutFwdOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:busOutFwdOctets.setStatus(_A)
_BusOutFwdUcastFrms_Type=Counter32
_BusOutFwdUcastFrms_Object=MibTableColumn
busOutFwdUcastFrms=_BusOutFwdUcastFrms_Object((1,3,6,1,4,1,9,9,40,1,1,1,13),_BusOutFwdUcastFrms_Type())
busOutFwdUcastFrms.setMaxAccess(_C)
if mibBuilder.loadTexts:busOutFwdUcastFrms.setStatus(_A)
_BusOutFwdNUcastFrms_Type=Counter32
_BusOutFwdNUcastFrms_Object=MibTableColumn
busOutFwdNUcastFrms=_BusOutFwdNUcastFrms_Object((1,3,6,1,4,1,9,9,40,1,1,1,14),_BusOutFwdNUcastFrms_Type())
busOutFwdNUcastFrms.setMaxAccess(_C)
if mibBuilder.loadTexts:busOutFwdNUcastFrms.setStatus(_A)
_BusFrmTimeOuts_Type=Counter32
_BusFrmTimeOuts_Object=MibTableColumn
busFrmTimeOuts=_BusFrmTimeOuts_Object((1,3,6,1,4,1,9,9,40,1,1,1,15),_BusFrmTimeOuts_Type())
busFrmTimeOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:busFrmTimeOuts.setStatus(_A)
_BusMultiFwdVpi_Type=CiscoVpiInteger
_BusMultiFwdVpi_Object=MibTableColumn
busMultiFwdVpi=_BusMultiFwdVpi_Object((1,3,6,1,4,1,9,9,40,1,1,1,16),_BusMultiFwdVpi_Type())
busMultiFwdVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:busMultiFwdVpi.setStatus(_A)
_BusMultiFwdVci_Type=CiscoVciInteger
_BusMultiFwdVci_Object=MibTableColumn
busMultiFwdVci=_BusMultiFwdVci_Object((1,3,6,1,4,1,9,9,40,1,1,1,17),_BusMultiFwdVci_Type())
busMultiFwdVci.setMaxAccess(_C)
if mibBuilder.loadTexts:busMultiFwdVci.setStatus(_A)
class _BusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_BusOperStatus_Type.__name__=_E
_BusOperStatus_Object=MibTableColumn
busOperStatus=_BusOperStatus_Object((1,3,6,1,4,1,9,9,40,1,1,1,18),_BusOperStatus_Type())
busOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:busOperStatus.setStatus(_A)
class _BusAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_BusAdminStatus_Type.__name__=_E
_BusAdminStatus_Object=MibTableColumn
busAdminStatus=_BusAdminStatus_Object((1,3,6,1,4,1,9,9,40,1,1,1,19),_BusAdminStatus_Type())
busAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:busAdminStatus.setStatus(_A)
_BusStatus_Type=RowStatus
_BusStatus_Object=MibTableColumn
busStatus=_BusStatus_Object((1,3,6,1,4,1,9,9,40,1,1,1,20),_BusStatus_Type())
busStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:busStatus.setStatus(_A)
_BusClientTable_Object=MibTable
busClientTable=_BusClientTable_Object((1,3,6,1,4,1,9,9,40,1,2))
if mibBuilder.loadTexts:busClientTable.setStatus(_A)
_BusClientEntry_Object=MibTableRow
busClientEntry=_BusClientEntry_Object((1,3,6,1,4,1,9,9,40,1,2,1))
busClientEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_M))
if mibBuilder.loadTexts:busClientEntry.setStatus(_A)
_BusClientId_Type=Integer32
_BusClientId_Object=MibTableColumn
busClientId=_BusClientId_Object((1,3,6,1,4,1,9,9,40,1,2,1,1),_BusClientId_Type())
busClientId.setMaxAccess(_H)
if mibBuilder.loadTexts:busClientId.setStatus(_A)
_BusClientIfIndex_Type=Integer32
_BusClientIfIndex_Object=MibTableColumn
busClientIfIndex=_BusClientIfIndex_Object((1,3,6,1,4,1,9,9,40,1,2,1,2),_BusClientIfIndex_Type())
busClientIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:busClientIfIndex.setStatus(_A)
_BusClientMSendVpi_Type=CiscoVpiInteger
_BusClientMSendVpi_Object=MibTableColumn
busClientMSendVpi=_BusClientMSendVpi_Object((1,3,6,1,4,1,9,9,40,1,2,1,3),_BusClientMSendVpi_Type())
busClientMSendVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:busClientMSendVpi.setStatus(_A)
_BusClientMSendVci_Type=CiscoVciInteger
_BusClientMSendVci_Object=MibTableColumn
busClientMSendVci=_BusClientMSendVci_Object((1,3,6,1,4,1,9,9,40,1,2,1,4),_BusClientMSendVci_Type())
busClientMSendVci.setMaxAccess(_C)
if mibBuilder.loadTexts:busClientMSendVci.setStatus(_A)
_BusClientAtmAddress_Type=AtmLaneAddress
_BusClientAtmAddress_Object=MibTableColumn
busClientAtmAddress=_BusClientAtmAddress_Object((1,3,6,1,4,1,9,9,40,1,2,1,5),_BusClientAtmAddress_Type())
busClientAtmAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:busClientAtmAddress.setStatus(_A)
_CiscoBusMIBConformance_ObjectIdentity=ObjectIdentity
ciscoBusMIBConformance=_CiscoBusMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,40,2))
_CiscoBusMIBGroups_ObjectIdentity=ObjectIdentity
ciscoBusMIBGroups=_CiscoBusMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,40,2,1))
_CiscoBusMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoBusMIBCompliances=_CiscoBusMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,40,2,2))
ciscoBusGroup=ObjectGroup((1,3,6,1,4,1,9,9,40,2,1,1))
ciscoBusGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ciscoBusGroup.setStatus(_A)
ciscoBusSubIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,40,2,1,2))
ciscoBusSubIfGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:ciscoBusSubIfGroup.setStatus(_A)
ciscoBusClientGroup=ObjectGroup((1,3,6,1,4,1,9,9,40,2,1,3))
ciscoBusClientGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:ciscoBusClientGroup.setStatus(_A)
ciscoBusMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,40,2,2,1))
ciscoBusMIBCompliance.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ciscoBusMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CiscoVpiInteger':CiscoVpiInteger,'CiscoVciInteger':CiscoVciInteger,'ciscoBusMIB':ciscoBusMIB,'ciscoBusMIBObjects':ciscoBusMIBObjects,'busTable':busTable,'busEntry':busEntry,_F:busElanName,_G:busIndex,_N:busAtmAddrSpec,_O:busAtmAddrMask,_P:busAtmAddrActl,_Q:busIfIndex,_e:busSubIfNum,_R:busUpTime,_S:busLanType,_T:busMaxFrm,_U:busMaxFrmAge,_V:busOutFwdOctets,_W:busOutFwdUcastFrms,_X:busOutFwdNUcastFrms,_Y:busFrmTimeOuts,_Z:busMultiFwdVpi,_a:busMultiFwdVci,_b:busOperStatus,_c:busAdminStatus,_d:busStatus,'busClientTable':busClientTable,'busClientEntry':busClientEntry,_M:busClientId,_f:busClientIfIndex,_g:busClientMSendVpi,_h:busClientMSendVci,_i:busClientAtmAddress,'ciscoBusMIBConformance':ciscoBusMIBConformance,'ciscoBusMIBGroups':ciscoBusMIBGroups,_j:ciscoBusGroup,_k:ciscoBusSubIfGroup,'ciscoBusClientGroup':ciscoBusClientGroup,'ciscoBusMIBCompliances':ciscoBusMIBCompliances,'ciscoBusMIBCompliance':ciscoBusMIBCompliance})