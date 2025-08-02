_i='vlanSflspLSDBFloodAdvSwitchID'
_h='vlanSflspLSDBFloodLSID'
_g='vlanSflspLSDBFloodType'
_f='vlanSflspLSDBFloodAreaID'
_e='vlanSflspTracePathListHopNum'
_d='vlanSflspTracePathListPathNum'
_c='vlanSflspTracePathListID'
_b='vlanSflspTracePathListDest'
_a='vlanSflspTracePathID'
_Z='vlanSflspTracePathDest'
_Y='suspend'
_X='activate'
_W='vlanSflsp1stHopDestSwitch'
_V='vlanSflspAreaAreaID'
_U='vlanSflspNeighborsPortName'
_T='vlanSflspIfMetricIfTOSType'
_S='vlanSflspIfMetricIfAddress'
_R='point-to-point'
_Q='vlanSflspInterfacesSwAddressLess'
_P='vlanSflspInterfacesIFAddress'
_O='vlanSflspLsdbSwitchID'
_N='vlanSflspLsdbLSID'
_M='vlanSflspLsdbType'
_L='vlanSflspLsdbAreaID'
_K='invalid'
_J='false'
_I='disabled'
_H='enabled'
_G='other'
_F='true'
_E='Integer32'
_D='CTRON-SFPS-SFLSP-MIB'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
vlanSflsp1stHop,vlanSflspArea,vlanSflspGeneralVariables,vlanSflspIfMetric,vlanSflspInterfaces,vlanSflspLSDBFlood,vlanSflspLSPStats,vlanSflspLsdb,vlanSflspNeighbors,vlanSflspTracePathAPI,vlanSflspTracePathInternal=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','vlanSflsp1stHop','vlanSflspArea','vlanSflspGeneralVariables','vlanSflspIfMetric','vlanSflspInterfaces','vlanSflspLSDBFlood','vlanSflspLSPStats','vlanSflspLsdb','vlanSflspNeighbors','vlanSflspTracePathAPI','vlanSflspTracePathInternal')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_VlanSflspGeneralSwitchID_Type=OctetString
_VlanSflspGeneralSwitchID_Object=MibScalar
vlanSflspGeneralSwitchID=_VlanSflspGeneralSwitchID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,1),_VlanSflspGeneralSwitchID_Type())
vlanSflspGeneralSwitchID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspGeneralSwitchID.setStatus(_A)
class _VlanSflspGeneralAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_VlanSflspGeneralAdminStatus_Type.__name__=_E
_VlanSflspGeneralAdminStatus_Object=MibScalar
vlanSflspGeneralAdminStatus=_VlanSflspGeneralAdminStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,2),_VlanSflspGeneralAdminStatus_Type())
vlanSflspGeneralAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspGeneralAdminStatus.setStatus(_A)
_VlanSflspGeneralVersion_Type=Integer32
_VlanSflspGeneralVersion_Object=MibScalar
vlanSflspGeneralVersion=_VlanSflspGeneralVersion_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,3),_VlanSflspGeneralVersion_Type())
vlanSflspGeneralVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspGeneralVersion.setStatus(_A)
class _VlanSflspGeneralAreaBRStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_J,2)))
_VlanSflspGeneralAreaBRStatus_Type.__name__=_E
_VlanSflspGeneralAreaBRStatus_Object=MibScalar
vlanSflspGeneralAreaBRStatus=_VlanSflspGeneralAreaBRStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,4),_VlanSflspGeneralAreaBRStatus_Type())
vlanSflspGeneralAreaBRStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspGeneralAreaBRStatus.setStatus(_A)
class _VlanSflspGeneralASBRStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_J,2)))
_VlanSflspGeneralASBRStatus_Type.__name__=_E
_VlanSflspGeneralASBRStatus_Object=MibScalar
vlanSflspGeneralASBRStatus=_VlanSflspGeneralASBRStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,5),_VlanSflspGeneralASBRStatus_Type())
vlanSflspGeneralASBRStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspGeneralASBRStatus.setStatus(_A)
class _VlanSflspGeneralTOSSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_J,2)))
_VlanSflspGeneralTOSSupport_Type.__name__=_E
_VlanSflspGeneralTOSSupport_Object=MibScalar
vlanSflspGeneralTOSSupport=_VlanSflspGeneralTOSSupport_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,6),_VlanSflspGeneralTOSSupport_Type())
vlanSflspGeneralTOSSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspGeneralTOSSupport.setStatus(_A)
_VlanSflspGeneralOrgNewLSAs_Type=Counter32
_VlanSflspGeneralOrgNewLSAs_Object=MibScalar
vlanSflspGeneralOrgNewLSAs=_VlanSflspGeneralOrgNewLSAs_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,7),_VlanSflspGeneralOrgNewLSAs_Type())
vlanSflspGeneralOrgNewLSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspGeneralOrgNewLSAs.setStatus(_A)
_VlanSflspGeneralRcvNewLSAs_Type=Counter32
_VlanSflspGeneralRcvNewLSAs_Object=MibScalar
vlanSflspGeneralRcvNewLSAs=_VlanSflspGeneralRcvNewLSAs_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,8),_VlanSflspGeneralRcvNewLSAs_Type())
vlanSflspGeneralRcvNewLSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspGeneralRcvNewLSAs.setStatus(_A)
_VlanSflspGeneralMaxOnQueue_Type=Integer32
_VlanSflspGeneralMaxOnQueue_Object=MibScalar
vlanSflspGeneralMaxOnQueue=_VlanSflspGeneralMaxOnQueue_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,9),_VlanSflspGeneralMaxOnQueue_Type())
vlanSflspGeneralMaxOnQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspGeneralMaxOnQueue.setStatus(_A)
_VlanSflspGeneralCurOnQueue_Type=Integer32
_VlanSflspGeneralCurOnQueue_Object=MibScalar
vlanSflspGeneralCurOnQueue=_VlanSflspGeneralCurOnQueue_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,10),_VlanSflspGeneralCurOnQueue_Type())
vlanSflspGeneralCurOnQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspGeneralCurOnQueue.setStatus(_A)
_VlanSflspGeneralMaxTimeUs_Type=Integer32
_VlanSflspGeneralMaxTimeUs_Object=MibScalar
vlanSflspGeneralMaxTimeUs=_VlanSflspGeneralMaxTimeUs_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,11),_VlanSflspGeneralMaxTimeUs_Type())
vlanSflspGeneralMaxTimeUs.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspGeneralMaxTimeUs.setStatus(_A)
_VlanSflspGeneralCurTimeUs_Type=Integer32
_VlanSflspGeneralCurTimeUs_Object=MibScalar
vlanSflspGeneralCurTimeUs=_VlanSflspGeneralCurTimeUs_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,12),_VlanSflspGeneralCurTimeUs_Type())
vlanSflspGeneralCurTimeUs.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspGeneralCurTimeUs.setStatus(_A)
_VlanSflspGeneralMaxEvents_Type=Integer32
_VlanSflspGeneralMaxEvents_Object=MibScalar
vlanSflspGeneralMaxEvents=_VlanSflspGeneralMaxEvents_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,13),_VlanSflspGeneralMaxEvents_Type())
vlanSflspGeneralMaxEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspGeneralMaxEvents.setStatus(_A)
_VlanSflspGeneralMaxTimeOccurred_Type=TimeTicks
_VlanSflspGeneralMaxTimeOccurred_Object=MibScalar
vlanSflspGeneralMaxTimeOccurred=_VlanSflspGeneralMaxTimeOccurred_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,14),_VlanSflspGeneralMaxTimeOccurred_Type())
vlanSflspGeneralMaxTimeOccurred.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspGeneralMaxTimeOccurred.setStatus(_A)
_VlanSflspGeneralMaxOnQOccurred_Type=TimeTicks
_VlanSflspGeneralMaxOnQOccurred_Object=MibScalar
vlanSflspGeneralMaxOnQOccurred=_VlanSflspGeneralMaxOnQOccurred_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,15),_VlanSflspGeneralMaxOnQOccurred_Type())
vlanSflspGeneralMaxOnQOccurred.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspGeneralMaxOnQOccurred.setStatus(_A)
_VlanSflspGeneralTotalSwLinks_Type=Integer32
_VlanSflspGeneralTotalSwLinks_Object=MibScalar
vlanSflspGeneralTotalSwLinks=_VlanSflspGeneralTotalSwLinks_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,16),_VlanSflspGeneralTotalSwLinks_Type())
vlanSflspGeneralTotalSwLinks.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspGeneralTotalSwLinks.setStatus(_A)
_VlanSflspGeneralLastChangeDet_Type=TimeTicks
_VlanSflspGeneralLastChangeDet_Object=MibScalar
vlanSflspGeneralLastChangeDet=_VlanSflspGeneralLastChangeDet_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,17),_VlanSflspGeneralLastChangeDet_Type())
vlanSflspGeneralLastChangeDet.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspGeneralLastChangeDet.setStatus(_A)
_VlanSflspGeneralFloodMask_Type=OctetString
_VlanSflspGeneralFloodMask_Object=MibScalar
vlanSflspGeneralFloodMask=_VlanSflspGeneralFloodMask_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,18),_VlanSflspGeneralFloodMask_Type())
vlanSflspGeneralFloodMask.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspGeneralFloodMask.setStatus(_A)
_VlanSflspGeneralLowestMac_Type=OctetString
_VlanSflspGeneralLowestMac_Object=MibScalar
vlanSflspGeneralLowestMac=_VlanSflspGeneralLowestMac_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,19),_VlanSflspGeneralLowestMac_Type())
vlanSflspGeneralLowestMac.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspGeneralLowestMac.setStatus(_A)
_VlanSflspGeneralRootId_Type=OctetString
_VlanSflspGeneralRootId_Object=MibScalar
vlanSflspGeneralRootId=_VlanSflspGeneralRootId_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,20),_VlanSflspGeneralRootId_Type())
vlanSflspGeneralRootId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspGeneralRootId.setStatus(_A)
class _VlanSflspGeneralFloodAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_VlanSflspGeneralFloodAdminStatus_Type.__name__=_E
_VlanSflspGeneralFloodAdminStatus_Object=MibScalar
vlanSflspGeneralFloodAdminStatus=_VlanSflspGeneralFloodAdminStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,1,1,21),_VlanSflspGeneralFloodAdminStatus_Type())
vlanSflspGeneralFloodAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspGeneralFloodAdminStatus.setStatus(_A)
_VlanSflspLsdbTable_Object=MibTable
vlanSflspLsdbTable=_VlanSflspLsdbTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,2,1))
if mibBuilder.loadTexts:vlanSflspLsdbTable.setStatus(_A)
_VlanSflspLsdbEntry_Object=MibTableRow
vlanSflspLsdbEntry=_VlanSflspLsdbEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,2,1,1))
vlanSflspLsdbEntry.setIndexNames((0,_D,_L),(0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:vlanSflspLsdbEntry.setStatus(_A)
_VlanSflspLsdbAreaID_Type=Integer32
_VlanSflspLsdbAreaID_Object=MibTableColumn
vlanSflspLsdbAreaID=_VlanSflspLsdbAreaID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,2,1,1,1),_VlanSflspLsdbAreaID_Type())
vlanSflspLsdbAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLsdbAreaID.setStatus(_A)
class _VlanSflspLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('switch-link',1),('connection-link',2)))
_VlanSflspLsdbType_Type.__name__=_E
_VlanSflspLsdbType_Object=MibTableColumn
vlanSflspLsdbType=_VlanSflspLsdbType_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,2,1,1,2),_VlanSflspLsdbType_Type())
vlanSflspLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLsdbType.setStatus(_A)
_VlanSflspLsdbLSID_Type=OctetString
_VlanSflspLsdbLSID_Object=MibTableColumn
vlanSflspLsdbLSID=_VlanSflspLsdbLSID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,2,1,1,3),_VlanSflspLsdbLSID_Type())
vlanSflspLsdbLSID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLsdbLSID.setStatus(_A)
_VlanSflspLsdbSwitchID_Type=OctetString
_VlanSflspLsdbSwitchID_Object=MibTableColumn
vlanSflspLsdbSwitchID=_VlanSflspLsdbSwitchID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,2,1,1,4),_VlanSflspLsdbSwitchID_Type())
vlanSflspLsdbSwitchID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLsdbSwitchID.setStatus(_A)
_VlanSflspLsdbSequence_Type=Integer32
_VlanSflspLsdbSequence_Object=MibTableColumn
vlanSflspLsdbSequence=_VlanSflspLsdbSequence_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,2,1,1,5),_VlanSflspLsdbSequence_Type())
vlanSflspLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLsdbSequence.setStatus(_A)
_VlanSflspLsdbAge_Type=Integer32
_VlanSflspLsdbAge_Object=MibTableColumn
vlanSflspLsdbAge=_VlanSflspLsdbAge_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,2,1,1,6),_VlanSflspLsdbAge_Type())
vlanSflspLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLsdbAge.setStatus(_A)
_VlanSflspLsdbChecksum_Type=Integer32
_VlanSflspLsdbChecksum_Object=MibTableColumn
vlanSflspLsdbChecksum=_VlanSflspLsdbChecksum_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,2,1,1,7),_VlanSflspLsdbChecksum_Type())
vlanSflspLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLsdbChecksum.setStatus(_A)
_VlanSflspLsdbAdvertisement_Type=OctetString
_VlanSflspLsdbAdvertisement_Object=MibTableColumn
vlanSflspLsdbAdvertisement=_VlanSflspLsdbAdvertisement_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,2,1,1,8),_VlanSflspLsdbAdvertisement_Type())
vlanSflspLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLsdbAdvertisement.setStatus(_A)
class _VlanSflspLsdbUsedInSPF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_F,1))
_VlanSflspLsdbUsedInSPF_Type.__name__=_E
_VlanSflspLsdbUsedInSPF_Object=MibTableColumn
vlanSflspLsdbUsedInSPF=_VlanSflspLsdbUsedInSPF_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,2,1,1,9),_VlanSflspLsdbUsedInSPF_Type())
vlanSflspLsdbUsedInSPF.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLsdbUsedInSPF.setStatus(_A)
_VlanSflspInterfacesTable_Object=MibTable
vlanSflspInterfacesTable=_VlanSflspInterfacesTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1))
if mibBuilder.loadTexts:vlanSflspInterfacesTable.setStatus(_A)
_VlanSflspInterfacesEntry_Object=MibTableRow
vlanSflspInterfacesEntry=_VlanSflspInterfacesEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1))
vlanSflspInterfacesEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:vlanSflspInterfacesEntry.setStatus(_A)
_VlanSflspInterfacesIFAddress_Type=SfpsAddress
_VlanSflspInterfacesIFAddress_Object=MibTableColumn
vlanSflspInterfacesIFAddress=_VlanSflspInterfacesIFAddress_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,1),_VlanSflspInterfacesIFAddress_Type())
vlanSflspInterfacesIFAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspInterfacesIFAddress.setStatus(_A)
_VlanSflspInterfacesSwAddressLess_Type=Integer32
_VlanSflspInterfacesSwAddressLess_Object=MibTableColumn
vlanSflspInterfacesSwAddressLess=_VlanSflspInterfacesSwAddressLess_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,2),_VlanSflspInterfacesSwAddressLess_Type())
vlanSflspInterfacesSwAddressLess.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspInterfacesSwAddressLess.setStatus(_A)
_VlanSflspInterfacesAreaID_Type=IpAddress
_VlanSflspInterfacesAreaID_Object=MibTableColumn
vlanSflspInterfacesAreaID=_VlanSflspInterfacesAreaID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,3),_VlanSflspInterfacesAreaID_Type())
vlanSflspInterfacesAreaID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspInterfacesAreaID.setStatus(_A)
class _VlanSflspInterfacesIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('brodcast',1),('nbma',2),(_R,3)))
_VlanSflspInterfacesIfType_Type.__name__=_E
_VlanSflspInterfacesIfType_Object=MibTableColumn
vlanSflspInterfacesIfType=_VlanSflspInterfacesIfType_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,4),_VlanSflspInterfacesIfType_Type())
vlanSflspInterfacesIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspInterfacesIfType.setStatus(_A)
class _VlanSflspInterfacesAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_VlanSflspInterfacesAdminStatus_Type.__name__=_E
_VlanSflspInterfacesAdminStatus_Object=MibTableColumn
vlanSflspInterfacesAdminStatus=_VlanSflspInterfacesAdminStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,5),_VlanSflspInterfacesAdminStatus_Type())
vlanSflspInterfacesAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspInterfacesAdminStatus.setStatus(_A)
_VlanSflspInterfacesSwPriority_Type=Integer32
_VlanSflspInterfacesSwPriority_Object=MibTableColumn
vlanSflspInterfacesSwPriority=_VlanSflspInterfacesSwPriority_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,6),_VlanSflspInterfacesSwPriority_Type())
vlanSflspInterfacesSwPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspInterfacesSwPriority.setStatus(_A)
_VlanSflspInterfacesTransDelay_Type=Integer32
_VlanSflspInterfacesTransDelay_Object=MibTableColumn
vlanSflspInterfacesTransDelay=_VlanSflspInterfacesTransDelay_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,7),_VlanSflspInterfacesTransDelay_Type())
vlanSflspInterfacesTransDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspInterfacesTransDelay.setStatus(_A)
_VlanSflspInterfacesReTransInterval_Type=Integer32
_VlanSflspInterfacesReTransInterval_Object=MibTableColumn
vlanSflspInterfacesReTransInterval=_VlanSflspInterfacesReTransInterval_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,8),_VlanSflspInterfacesReTransInterval_Type())
vlanSflspInterfacesReTransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspInterfacesReTransInterval.setStatus(_A)
_VlanSflspInterfacesHelloInterval_Type=Integer32
_VlanSflspInterfacesHelloInterval_Object=MibTableColumn
vlanSflspInterfacesHelloInterval=_VlanSflspInterfacesHelloInterval_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,9),_VlanSflspInterfacesHelloInterval_Type())
vlanSflspInterfacesHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspInterfacesHelloInterval.setStatus(_A)
_VlanSflspInterfacesDeadInterval_Type=Integer32
_VlanSflspInterfacesDeadInterval_Object=MibTableColumn
vlanSflspInterfacesDeadInterval=_VlanSflspInterfacesDeadInterval_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,10),_VlanSflspInterfacesDeadInterval_Type())
vlanSflspInterfacesDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspInterfacesDeadInterval.setStatus(_A)
_VlanSflspInterfacesPollInterval_Type=Integer32
_VlanSflspInterfacesPollInterval_Object=MibTableColumn
vlanSflspInterfacesPollInterval=_VlanSflspInterfacesPollInterval_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,11),_VlanSflspInterfacesPollInterval_Type())
vlanSflspInterfacesPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspInterfacesPollInterval.setStatus(_A)
class _VlanSflspInterfacesState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('down',1),('loopback',2),('waiting',3),(_R,4),('dr',5),('bdr',6),('dr-other',7)))
_VlanSflspInterfacesState_Type.__name__=_E
_VlanSflspInterfacesState_Object=MibTableColumn
vlanSflspInterfacesState=_VlanSflspInterfacesState_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,12),_VlanSflspInterfacesState_Type())
vlanSflspInterfacesState.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspInterfacesState.setStatus(_A)
_VlanSflspInterfacesDS_Type=SfpsAddress
_VlanSflspInterfacesDS_Object=MibTableColumn
vlanSflspInterfacesDS=_VlanSflspInterfacesDS_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,13),_VlanSflspInterfacesDS_Type())
vlanSflspInterfacesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspInterfacesDS.setStatus(_A)
_VlanSflspInterfacesBDS_Type=SfpsAddress
_VlanSflspInterfacesBDS_Object=MibTableColumn
vlanSflspInterfacesBDS=_VlanSflspInterfacesBDS_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,14),_VlanSflspInterfacesBDS_Type())
vlanSflspInterfacesBDS.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspInterfacesBDS.setStatus(_A)
_VlanSflspInterfacesEvents_Type=Counter32
_VlanSflspInterfacesEvents_Object=MibTableColumn
vlanSflspInterfacesEvents=_VlanSflspInterfacesEvents_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,15),_VlanSflspInterfacesEvents_Type())
vlanSflspInterfacesEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspInterfacesEvents.setStatus(_A)
_VlanSflspInterfacesAuthKey_Type=SfpsAddress
_VlanSflspInterfacesAuthKey_Object=MibTableColumn
vlanSflspInterfacesAuthKey=_VlanSflspInterfacesAuthKey_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,3,1,1,16),_VlanSflspInterfacesAuthKey_Type())
vlanSflspInterfacesAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspInterfacesAuthKey.setStatus(_A)
_VlanSflspIfMetricTable_Object=MibTable
vlanSflspIfMetricTable=_VlanSflspIfMetricTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,4,1))
if mibBuilder.loadTexts:vlanSflspIfMetricTable.setStatus(_A)
_VlanSflspIfMetricEntry_Object=MibTableRow
vlanSflspIfMetricEntry=_VlanSflspIfMetricEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,4,1,1))
vlanSflspIfMetricEntry.setIndexNames((0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:vlanSflspIfMetricEntry.setStatus(_A)
_VlanSflspIfMetricIfAddress_Type=OctetString
_VlanSflspIfMetricIfAddress_Object=MibTableColumn
vlanSflspIfMetricIfAddress=_VlanSflspIfMetricIfAddress_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,4,1,1,1),_VlanSflspIfMetricIfAddress_Type())
vlanSflspIfMetricIfAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspIfMetricIfAddress.setStatus(_A)
_VlanSflspIfMetricIfTOSType_Type=Integer32
_VlanSflspIfMetricIfTOSType_Object=MibTableColumn
vlanSflspIfMetricIfTOSType=_VlanSflspIfMetricIfTOSType_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,4,1,1,2),_VlanSflspIfMetricIfTOSType_Type())
vlanSflspIfMetricIfTOSType.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspIfMetricIfTOSType.setStatus(_A)
_VlanSflspIfMetricIfMetric_Type=Integer32
_VlanSflspIfMetricIfMetric_Object=MibTableColumn
vlanSflspIfMetricIfMetric=_VlanSflspIfMetricIfMetric_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,4,1,1,3),_VlanSflspIfMetricIfMetric_Type())
vlanSflspIfMetricIfMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspIfMetricIfMetric.setStatus(_A)
class _VlanSflspIfMetricIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_K,2)))
_VlanSflspIfMetricIfStatus_Type.__name__=_E
_VlanSflspIfMetricIfStatus_Object=MibTableColumn
vlanSflspIfMetricIfStatus=_VlanSflspIfMetricIfStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,4,1,1,4),_VlanSflspIfMetricIfStatus_Type())
vlanSflspIfMetricIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspIfMetricIfStatus.setStatus(_A)
_VlanSflspNeighborsTable_Object=MibTable
vlanSflspNeighborsTable=_VlanSflspNeighborsTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1))
if mibBuilder.loadTexts:vlanSflspNeighborsTable.setStatus(_A)
_VlanSflspNeighborsEntry_Object=MibTableRow
vlanSflspNeighborsEntry=_VlanSflspNeighborsEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1))
vlanSflspNeighborsEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:vlanSflspNeighborsEntry.setStatus(_A)
_VlanSflspNeighborsPortName_Type=OctetString
_VlanSflspNeighborsPortName_Object=MibTableColumn
vlanSflspNeighborsPortName=_VlanSflspNeighborsPortName_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,1),_VlanSflspNeighborsPortName_Type())
vlanSflspNeighborsPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsPortName.setStatus(_A)
_VlanSflspNeighborsSwitchID_Type=OctetString
_VlanSflspNeighborsSwitchID_Object=MibTableColumn
vlanSflspNeighborsSwitchID=_VlanSflspNeighborsSwitchID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,2),_VlanSflspNeighborsSwitchID_Type())
vlanSflspNeighborsSwitchID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsSwitchID.setStatus(_A)
_VlanSflspNeighborsOptions_Type=Integer32
_VlanSflspNeighborsOptions_Object=MibTableColumn
vlanSflspNeighborsOptions=_VlanSflspNeighborsOptions_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,3),_VlanSflspNeighborsOptions_Type())
vlanSflspNeighborsOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsOptions.setStatus(_A)
_VlanSflspNeighborsPriority_Type=Integer32
_VlanSflspNeighborsPriority_Object=MibTableColumn
vlanSflspNeighborsPriority=_VlanSflspNeighborsPriority_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,4),_VlanSflspNeighborsPriority_Type())
vlanSflspNeighborsPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsPriority.setStatus(_A)
class _VlanSflspNeighborsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('down',1),('attempt',2),('init',3),('two-way',4),('exchange',5),('exchange-start',6),('loading',7),('full',8)))
_VlanSflspNeighborsState_Type.__name__=_E
_VlanSflspNeighborsState_Object=MibTableColumn
vlanSflspNeighborsState=_VlanSflspNeighborsState_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,5),_VlanSflspNeighborsState_Type())
vlanSflspNeighborsState.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsState.setStatus(_A)
_VlanSflspNeighborsEvents_Type=Counter32
_VlanSflspNeighborsEvents_Object=MibTableColumn
vlanSflspNeighborsEvents=_VlanSflspNeighborsEvents_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,6),_VlanSflspNeighborsEvents_Type())
vlanSflspNeighborsEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsEvents.setStatus(_A)
_VlanSflspNeighborsLSRetransQLen_Type=Gauge32
_VlanSflspNeighborsLSRetransQLen_Object=MibTableColumn
vlanSflspNeighborsLSRetransQLen=_VlanSflspNeighborsLSRetransQLen_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,7),_VlanSflspNeighborsLSRetransQLen_Type())
vlanSflspNeighborsLSRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsLSRetransQLen.setStatus(_A)
_VlanSflspNeighborsHELLOsRcvd_Type=Integer32
_VlanSflspNeighborsHELLOsRcvd_Object=MibTableColumn
vlanSflspNeighborsHELLOsRcvd=_VlanSflspNeighborsHELLOsRcvd_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,8),_VlanSflspNeighborsHELLOsRcvd_Type())
vlanSflspNeighborsHELLOsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsHELLOsRcvd.setStatus(_A)
_VlanSflspNeighborsDBDsRcvd_Type=Integer32
_VlanSflspNeighborsDBDsRcvd_Object=MibTableColumn
vlanSflspNeighborsDBDsRcvd=_VlanSflspNeighborsDBDsRcvd_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,9),_VlanSflspNeighborsDBDsRcvd_Type())
vlanSflspNeighborsDBDsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsDBDsRcvd.setStatus(_A)
_VlanSflspNeighborsLSUsRcvd_Type=Integer32
_VlanSflspNeighborsLSUsRcvd_Object=MibTableColumn
vlanSflspNeighborsLSUsRcvd=_VlanSflspNeighborsLSUsRcvd_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,10),_VlanSflspNeighborsLSUsRcvd_Type())
vlanSflspNeighborsLSUsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsLSUsRcvd.setStatus(_A)
_VlanSflspNeighborsLSRsRcvd_Type=Integer32
_VlanSflspNeighborsLSRsRcvd_Object=MibTableColumn
vlanSflspNeighborsLSRsRcvd=_VlanSflspNeighborsLSRsRcvd_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,11),_VlanSflspNeighborsLSRsRcvd_Type())
vlanSflspNeighborsLSRsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsLSRsRcvd.setStatus(_A)
_VlanSflspNeighborsLSACKsRcvd_Type=Integer32
_VlanSflspNeighborsLSACKsRcvd_Object=MibTableColumn
vlanSflspNeighborsLSACKsRcvd=_VlanSflspNeighborsLSACKsRcvd_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,12),_VlanSflspNeighborsLSACKsRcvd_Type())
vlanSflspNeighborsLSACKsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsLSACKsRcvd.setStatus(_A)
_VlanSflspNeighborsHELLOsSent_Type=Integer32
_VlanSflspNeighborsHELLOsSent_Object=MibTableColumn
vlanSflspNeighborsHELLOsSent=_VlanSflspNeighborsHELLOsSent_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,13),_VlanSflspNeighborsHELLOsSent_Type())
vlanSflspNeighborsHELLOsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsHELLOsSent.setStatus(_A)
_VlanSflspNeighborsDBDsSent_Type=Integer32
_VlanSflspNeighborsDBDsSent_Object=MibTableColumn
vlanSflspNeighborsDBDsSent=_VlanSflspNeighborsDBDsSent_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,14),_VlanSflspNeighborsDBDsSent_Type())
vlanSflspNeighborsDBDsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsDBDsSent.setStatus(_A)
_VlanSflspNeighborsLSUsSent_Type=Integer32
_VlanSflspNeighborsLSUsSent_Object=MibTableColumn
vlanSflspNeighborsLSUsSent=_VlanSflspNeighborsLSUsSent_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,15),_VlanSflspNeighborsLSUsSent_Type())
vlanSflspNeighborsLSUsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsLSUsSent.setStatus(_A)
_VlanSflspNeighborsLSRsSent_Type=Integer32
_VlanSflspNeighborsLSRsSent_Object=MibTableColumn
vlanSflspNeighborsLSRsSent=_VlanSflspNeighborsLSRsSent_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,16),_VlanSflspNeighborsLSRsSent_Type())
vlanSflspNeighborsLSRsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsLSRsSent.setStatus(_A)
_VlanSflspNeighborsLSACKsSent_Type=Integer32
_VlanSflspNeighborsLSACKsSent_Object=MibTableColumn
vlanSflspNeighborsLSACKsSent=_VlanSflspNeighborsLSACKsSent_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,17),_VlanSflspNeighborsLSACKsSent_Type())
vlanSflspNeighborsLSACKsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsLSACKsSent.setStatus(_A)
class _VlanSflspNeighborsNBMAStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_K,2)))
_VlanSflspNeighborsNBMAStatus_Type.__name__=_E
_VlanSflspNeighborsNBMAStatus_Object=MibTableColumn
vlanSflspNeighborsNBMAStatus=_VlanSflspNeighborsNBMAStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,18),_VlanSflspNeighborsNBMAStatus_Type())
vlanSflspNeighborsNBMAStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsNBMAStatus.setStatus(_A)
_VlanSflspNeighborsFULLTimeSec_Type=TimeTicks
_VlanSflspNeighborsFULLTimeSec_Object=MibTableColumn
vlanSflspNeighborsFULLTimeSec=_VlanSflspNeighborsFULLTimeSec_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,5,1,1,19),_VlanSflspNeighborsFULLTimeSec_Type())
vlanSflspNeighborsFULLTimeSec.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspNeighborsFULLTimeSec.setStatus(_A)
_VlanSflspAreaTable_Object=MibTable
vlanSflspAreaTable=_VlanSflspAreaTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,6,1))
if mibBuilder.loadTexts:vlanSflspAreaTable.setStatus(_A)
_VlanSflspAreaEntry_Object=MibTableRow
vlanSflspAreaEntry=_VlanSflspAreaEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,6,1,1))
vlanSflspAreaEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:vlanSflspAreaEntry.setStatus(_A)
_VlanSflspAreaAreaID_Type=IpAddress
_VlanSflspAreaAreaID_Object=MibTableColumn
vlanSflspAreaAreaID=_VlanSflspAreaAreaID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,6,1,1,1),_VlanSflspAreaAreaID_Type())
vlanSflspAreaAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspAreaAreaID.setStatus(_A)
_VlanSflspAreaAuthType_Type=Integer32
_VlanSflspAreaAuthType_Object=MibTableColumn
vlanSflspAreaAuthType=_VlanSflspAreaAuthType_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,6,1,1,2),_VlanSflspAreaAuthType_Type())
vlanSflspAreaAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspAreaAuthType.setStatus(_A)
_VlanSflspAreaSPFRuns_Type=Counter32
_VlanSflspAreaSPFRuns_Object=MibTableColumn
vlanSflspAreaSPFRuns=_VlanSflspAreaSPFRuns_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,6,1,1,3),_VlanSflspAreaSPFRuns_Type())
vlanSflspAreaSPFRuns.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspAreaSPFRuns.setStatus(_A)
_VlanSflspAreaABRCount_Type=Gauge32
_VlanSflspAreaABRCount_Object=MibTableColumn
vlanSflspAreaABRCount=_VlanSflspAreaABRCount_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,6,1,1,4),_VlanSflspAreaABRCount_Type())
vlanSflspAreaABRCount.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspAreaABRCount.setStatus(_A)
_VlanSflspAreaASBRCount_Type=Gauge32
_VlanSflspAreaASBRCount_Object=MibTableColumn
vlanSflspAreaASBRCount=_VlanSflspAreaASBRCount_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,6,1,1,5),_VlanSflspAreaASBRCount_Type())
vlanSflspAreaASBRCount.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspAreaASBRCount.setStatus(_A)
_VlanSflspAreaAreaLSACnt_Type=Gauge32
_VlanSflspAreaAreaLSACnt_Object=MibTableColumn
vlanSflspAreaAreaLSACnt=_VlanSflspAreaAreaLSACnt_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,6,1,1,6),_VlanSflspAreaAreaLSACnt_Type())
vlanSflspAreaAreaLSACnt.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspAreaAreaLSACnt.setStatus(_A)
_VlanSflspAreaAreaCheckSum_Type=Integer32
_VlanSflspAreaAreaCheckSum_Object=MibTableColumn
vlanSflspAreaAreaCheckSum=_VlanSflspAreaAreaCheckSum_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,6,1,1,7),_VlanSflspAreaAreaCheckSum_Type())
vlanSflspAreaAreaCheckSum.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspAreaAreaCheckSum.setStatus(_A)
_VlanSflspAreaLastSpfRun_Type=TimeTicks
_VlanSflspAreaLastSpfRun_Object=MibTableColumn
vlanSflspAreaLastSpfRun=_VlanSflspAreaLastSpfRun_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,6,1,1,8),_VlanSflspAreaLastSpfRun_Type())
vlanSflspAreaLastSpfRun.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspAreaLastSpfRun.setStatus(_A)
_VlanSflsp1stHopTable_Object=MibTable
vlanSflsp1stHopTable=_VlanSflsp1stHopTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,7,1))
if mibBuilder.loadTexts:vlanSflsp1stHopTable.setStatus(_A)
_VlanSflsp1stHopEntry_Object=MibTableRow
vlanSflsp1stHopEntry=_VlanSflsp1stHopEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,7,1,1))
vlanSflsp1stHopEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:vlanSflsp1stHopEntry.setStatus(_A)
_VlanSflsp1stHopDestSwitch_Type=OctetString
_VlanSflsp1stHopDestSwitch_Object=MibTableColumn
vlanSflsp1stHopDestSwitch=_VlanSflsp1stHopDestSwitch_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,7,1,1,1),_VlanSflsp1stHopDestSwitch_Type())
vlanSflsp1stHopDestSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflsp1stHopDestSwitch.setStatus(_A)
_VlanSflsp1stHopPath11stHop_Type=OctetString
_VlanSflsp1stHopPath11stHop_Object=MibTableColumn
vlanSflsp1stHopPath11stHop=_VlanSflsp1stHopPath11stHop_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,7,1,1,2),_VlanSflsp1stHopPath11stHop_Type())
vlanSflsp1stHopPath11stHop.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflsp1stHopPath11stHop.setStatus(_A)
_VlanSflsp1stHopPath21stHop_Type=OctetString
_VlanSflsp1stHopPath21stHop_Object=MibTableColumn
vlanSflsp1stHopPath21stHop=_VlanSflsp1stHopPath21stHop_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,7,1,1,3),_VlanSflsp1stHopPath21stHop_Type())
vlanSflsp1stHopPath21stHop.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflsp1stHopPath21stHop.setStatus(_A)
_VlanSflsp1stHopPath31stHop_Type=OctetString
_VlanSflsp1stHopPath31stHop_Object=MibTableColumn
vlanSflsp1stHopPath31stHop=_VlanSflsp1stHopPath31stHop_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,7,1,1,4),_VlanSflsp1stHopPath31stHop_Type())
vlanSflsp1stHopPath31stHop.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflsp1stHopPath31stHop.setStatus(_A)
_VlanSflspTracePathAPIDest_Type=OctetString
_VlanSflspTracePathAPIDest_Object=MibScalar
vlanSflspTracePathAPIDest=_VlanSflspTracePathAPIDest_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,1,1,1),_VlanSflspTracePathAPIDest_Type())
vlanSflspTracePathAPIDest.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspTracePathAPIDest.setStatus(_A)
_VlanSflspTracePathAPIID_Type=Integer32
_VlanSflspTracePathAPIID_Object=MibScalar
vlanSflspTracePathAPIID=_VlanSflspTracePathAPIID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,1,1,2),_VlanSflspTracePathAPIID_Type())
vlanSflspTracePathAPIID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspTracePathAPIID.setStatus(_A)
class _VlanSflspTracePathAPIType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_K,2)))
_VlanSflspTracePathAPIType_Type.__name__=_E
_VlanSflspTracePathAPIType_Object=MibScalar
vlanSflspTracePathAPIType=_VlanSflspTracePathAPIType_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,1,1,3),_VlanSflspTracePathAPIType_Type())
vlanSflspTracePathAPIType.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspTracePathAPIType.setStatus(_A)
class _VlanSflspTracePathAPIAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_X,2),(_Y,3)))
_VlanSflspTracePathAPIAction_Type.__name__=_E
_VlanSflspTracePathAPIAction_Object=MibScalar
vlanSflspTracePathAPIAction=_VlanSflspTracePathAPIAction_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,1,1,4),_VlanSflspTracePathAPIAction_Type())
vlanSflspTracePathAPIAction.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspTracePathAPIAction.setStatus(_A)
_VlanSflspTracePathTable_Object=MibTable
vlanSflspTracePathTable=_VlanSflspTracePathTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,1))
if mibBuilder.loadTexts:vlanSflspTracePathTable.setStatus(_A)
_VlanSflspTracePathEntry_Object=MibTableRow
vlanSflspTracePathEntry=_VlanSflspTracePathEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,1,1))
vlanSflspTracePathEntry.setIndexNames((0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:vlanSflspTracePathEntry.setStatus(_A)
_VlanSflspTracePathDest_Type=OctetString
_VlanSflspTracePathDest_Object=MibTableColumn
vlanSflspTracePathDest=_VlanSflspTracePathDest_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,1,1,1),_VlanSflspTracePathDest_Type())
vlanSflspTracePathDest.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspTracePathDest.setStatus(_A)
_VlanSflspTracePathID_Type=Integer32
_VlanSflspTracePathID_Object=MibTableColumn
vlanSflspTracePathID=_VlanSflspTracePathID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,1,1,2),_VlanSflspTracePathID_Type())
vlanSflspTracePathID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspTracePathID.setStatus(_A)
class _VlanSflspTracePathAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_X,2),(_Y,3)))
_VlanSflspTracePathAction_Type.__name__=_E
_VlanSflspTracePathAction_Object=MibTableColumn
vlanSflspTracePathAction=_VlanSflspTracePathAction_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,1,1,3),_VlanSflspTracePathAction_Type())
vlanSflspTracePathAction.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspTracePathAction.setStatus(_A)
class _VlanSflspTracePathStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('success',2),('failed',3)))
_VlanSflspTracePathStatus_Type.__name__=_E
_VlanSflspTracePathStatus_Object=MibTableColumn
vlanSflspTracePathStatus=_VlanSflspTracePathStatus_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,1,1,4),_VlanSflspTracePathStatus_Type())
vlanSflspTracePathStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspTracePathStatus.setStatus(_A)
_VlanSflspTracePathListTable_Object=MibTable
vlanSflspTracePathListTable=_VlanSflspTracePathListTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,2))
if mibBuilder.loadTexts:vlanSflspTracePathListTable.setStatus(_A)
_VlanSflspTracePathListEntry_Object=MibTableRow
vlanSflspTracePathListEntry=_VlanSflspTracePathListEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,2,1))
vlanSflspTracePathListEntry.setIndexNames((0,_D,_b),(0,_D,_c),(0,_D,_d),(0,_D,_e))
if mibBuilder.loadTexts:vlanSflspTracePathListEntry.setStatus(_A)
_VlanSflspTracePathListDest_Type=OctetString
_VlanSflspTracePathListDest_Object=MibTableColumn
vlanSflspTracePathListDest=_VlanSflspTracePathListDest_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,2,1,1),_VlanSflspTracePathListDest_Type())
vlanSflspTracePathListDest.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspTracePathListDest.setStatus(_A)
_VlanSflspTracePathListID_Type=Integer32
_VlanSflspTracePathListID_Object=MibTableColumn
vlanSflspTracePathListID=_VlanSflspTracePathListID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,2,1,2),_VlanSflspTracePathListID_Type())
vlanSflspTracePathListID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspTracePathListID.setStatus(_A)
_VlanSflspTracePathListPathNum_Type=Integer32
_VlanSflspTracePathListPathNum_Object=MibTableColumn
vlanSflspTracePathListPathNum=_VlanSflspTracePathListPathNum_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,2,1,3),_VlanSflspTracePathListPathNum_Type())
vlanSflspTracePathListPathNum.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspTracePathListPathNum.setStatus(_A)
_VlanSflspTracePathListHopNum_Type=Integer32
_VlanSflspTracePathListHopNum_Object=MibTableColumn
vlanSflspTracePathListHopNum=_VlanSflspTracePathListHopNum_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,2,1,4),_VlanSflspTracePathListHopNum_Type())
vlanSflspTracePathListHopNum.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspTracePathListHopNum.setStatus(_A)
_VlanSflspTracePathListHopAddr_Type=OctetString
_VlanSflspTracePathListHopAddr_Object=MibTableColumn
vlanSflspTracePathListHopAddr=_VlanSflspTracePathListHopAddr_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,8,2,2,1,5),_VlanSflspTracePathListHopAddr_Type())
vlanSflspTracePathListHopAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspTracePathListHopAddr.setStatus(_A)
_VlanSflspLSDBFloodTable_Object=MibTable
vlanSflspLSDBFloodTable=_VlanSflspLSDBFloodTable_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,20,1))
if mibBuilder.loadTexts:vlanSflspLSDBFloodTable.setStatus(_A)
_VlanSflspLSDBFloodEntry_Object=MibTableRow
vlanSflspLSDBFloodEntry=_VlanSflspLSDBFloodEntry_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,20,1,1))
vlanSflspLSDBFloodEntry.setIndexNames((0,_D,_f),(0,_D,_g),(0,_D,_h),(0,_D,_i))
if mibBuilder.loadTexts:vlanSflspLSDBFloodEntry.setStatus(_A)
_VlanSflspLSDBFloodAreaID_Type=Integer32
_VlanSflspLSDBFloodAreaID_Object=MibTableColumn
vlanSflspLSDBFloodAreaID=_VlanSflspLSDBFloodAreaID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,20,1,1,1),_VlanSflspLSDBFloodAreaID_Type())
vlanSflspLSDBFloodAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSDBFloodAreaID.setStatus(_A)
class _VlanSflspLSDBFloodType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('switchLink',1),('connectionLink',2)))
_VlanSflspLSDBFloodType_Type.__name__=_E
_VlanSflspLSDBFloodType_Object=MibTableColumn
vlanSflspLSDBFloodType=_VlanSflspLSDBFloodType_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,20,1,1,2),_VlanSflspLSDBFloodType_Type())
vlanSflspLSDBFloodType.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSDBFloodType.setStatus(_A)
_VlanSflspLSDBFloodLSID_Type=SfpsAddress
_VlanSflspLSDBFloodLSID_Object=MibTableColumn
vlanSflspLSDBFloodLSID=_VlanSflspLSDBFloodLSID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,20,1,1,3),_VlanSflspLSDBFloodLSID_Type())
vlanSflspLSDBFloodLSID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSDBFloodLSID.setStatus(_A)
_VlanSflspLSDBFloodAdvSwitchID_Type=SfpsAddress
_VlanSflspLSDBFloodAdvSwitchID_Object=MibTableColumn
vlanSflspLSDBFloodAdvSwitchID=_VlanSflspLSDBFloodAdvSwitchID_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,20,1,1,4),_VlanSflspLSDBFloodAdvSwitchID_Type())
vlanSflspLSDBFloodAdvSwitchID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSDBFloodAdvSwitchID.setStatus(_A)
_VlanSflspLSDBFloodSequence_Type=Integer32
_VlanSflspLSDBFloodSequence_Object=MibTableColumn
vlanSflspLSDBFloodSequence=_VlanSflspLSDBFloodSequence_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,20,1,1,5),_VlanSflspLSDBFloodSequence_Type())
vlanSflspLSDBFloodSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSDBFloodSequence.setStatus(_A)
_VlanSflspLSDBFloodAge_Type=Integer32
_VlanSflspLSDBFloodAge_Object=MibTableColumn
vlanSflspLSDBFloodAge=_VlanSflspLSDBFloodAge_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,20,1,1,6),_VlanSflspLSDBFloodAge_Type())
vlanSflspLSDBFloodAge.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSDBFloodAge.setStatus(_A)
_VlanSflspLSDBFloodChecksum_Type=Integer32
_VlanSflspLSDBFloodChecksum_Object=MibTableColumn
vlanSflspLSDBFloodChecksum=_VlanSflspLSDBFloodChecksum_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,20,1,1,7),_VlanSflspLSDBFloodChecksum_Type())
vlanSflspLSDBFloodChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSDBFloodChecksum.setStatus(_A)
_VlanSflspLSDBFloodAdvertisement_Type=SfpsAddress
_VlanSflspLSDBFloodAdvertisement_Object=MibTableColumn
vlanSflspLSDBFloodAdvertisement=_VlanSflspLSDBFloodAdvertisement_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,20,1,1,8),_VlanSflspLSDBFloodAdvertisement_Type())
vlanSflspLSDBFloodAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSDBFloodAdvertisement.setStatus(_A)
class _VlanSflspLSDBFloodUsedInSPF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_F,1))
_VlanSflspLSDBFloodUsedInSPF_Type.__name__=_E
_VlanSflspLSDBFloodUsedInSPF_Object=MibTableColumn
vlanSflspLSDBFloodUsedInSPF=_VlanSflspLSDBFloodUsedInSPF_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,20,1,1,9),_VlanSflspLSDBFloodUsedInSPF_Type())
vlanSflspLSDBFloodUsedInSPF.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSDBFloodUsedInSPF.setStatus(_A)
class _VlanSflspLSDBFloodEverUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_F,1))
_VlanSflspLSDBFloodEverUsed_Type.__name__=_E
_VlanSflspLSDBFloodEverUsed_Object=MibTableColumn
vlanSflspLSDBFloodEverUsed=_VlanSflspLSDBFloodEverUsed_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,20,1,1,10),_VlanSflspLSDBFloodEverUsed_Type())
vlanSflspLSDBFloodEverUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSDBFloodEverUsed.setStatus(_A)
_VlanSflspLSPStatsMaxOnQueue_Type=Integer32
_VlanSflspLSPStatsMaxOnQueue_Object=MibScalar
vlanSflspLSPStatsMaxOnQueue=_VlanSflspLSPStatsMaxOnQueue_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,1),_VlanSflspLSPStatsMaxOnQueue_Type())
vlanSflspLSPStatsMaxOnQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsMaxOnQueue.setStatus(_A)
_VlanSflspLSPStatsCurOnQueue_Type=Integer32
_VlanSflspLSPStatsCurOnQueue_Object=MibScalar
vlanSflspLSPStatsCurOnQueue=_VlanSflspLSPStatsCurOnQueue_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,2),_VlanSflspLSPStatsCurOnQueue_Type())
vlanSflspLSPStatsCurOnQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsCurOnQueue.setStatus(_A)
_VlanSflspLSPStatsMaxTimeUs_Type=Integer32
_VlanSflspLSPStatsMaxTimeUs_Object=MibScalar
vlanSflspLSPStatsMaxTimeUs=_VlanSflspLSPStatsMaxTimeUs_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,3),_VlanSflspLSPStatsMaxTimeUs_Type())
vlanSflspLSPStatsMaxTimeUs.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsMaxTimeUs.setStatus(_A)
_VlanSflspLSPStatsCurTimeUs_Type=Integer32
_VlanSflspLSPStatsCurTimeUs_Object=MibScalar
vlanSflspLSPStatsCurTimeUs=_VlanSflspLSPStatsCurTimeUs_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,4),_VlanSflspLSPStatsCurTimeUs_Type())
vlanSflspLSPStatsCurTimeUs.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsCurTimeUs.setStatus(_A)
_VlanSflspLSPStatsMaxTimeOccurred_Type=Integer32
_VlanSflspLSPStatsMaxTimeOccurred_Object=MibScalar
vlanSflspLSPStatsMaxTimeOccurred=_VlanSflspLSPStatsMaxTimeOccurred_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,5),_VlanSflspLSPStatsMaxTimeOccurred_Type())
vlanSflspLSPStatsMaxTimeOccurred.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsMaxTimeOccurred.setStatus(_A)
_VlanSflspLSPStatsMaxOnQOccurred_Type=TimeTicks
_VlanSflspLSPStatsMaxOnQOccurred_Object=MibScalar
vlanSflspLSPStatsMaxOnQOccurred=_VlanSflspLSPStatsMaxOnQOccurred_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,6),_VlanSflspLSPStatsMaxOnQOccurred_Type())
vlanSflspLSPStatsMaxOnQOccurred.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsMaxOnQOccurred.setStatus(_A)
_VlanSflspLSPStatsTotalSwLinks_Type=Integer32
_VlanSflspLSPStatsTotalSwLinks_Object=MibScalar
vlanSflspLSPStatsTotalSwLinks=_VlanSflspLSPStatsTotalSwLinks_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,7),_VlanSflspLSPStatsTotalSwLinks_Type())
vlanSflspLSPStatsTotalSwLinks.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsTotalSwLinks.setStatus(_A)
_VlanSflspLSPStatsLastChangeDet_Type=TimeTicks
_VlanSflspLSPStatsLastChangeDet_Object=MibScalar
vlanSflspLSPStatsLastChangeDet=_VlanSflspLSPStatsLastChangeDet_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,8),_VlanSflspLSPStatsLastChangeDet_Type())
vlanSflspLSPStatsLastChangeDet.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsLastChangeDet.setStatus(_A)
_VlanSflspLSPStatsNumSPFRuns_Type=Integer32
_VlanSflspLSPStatsNumSPFRuns_Object=MibScalar
vlanSflspLSPStatsNumSPFRuns=_VlanSflspLSPStatsNumSPFRuns_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,9),_VlanSflspLSPStatsNumSPFRuns_Type())
vlanSflspLSPStatsNumSPFRuns.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSflspLSPStatsNumSPFRuns.setStatus(_A)
_VlanSflspLSPStatsNumFULLNbrs_Type=Integer32
_VlanSflspLSPStatsNumFULLNbrs_Object=MibScalar
vlanSflspLSPStatsNumFULLNbrs=_VlanSflspLSPStatsNumFULLNbrs_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,10),_VlanSflspLSPStatsNumFULLNbrs_Type())
vlanSflspLSPStatsNumFULLNbrs.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsNumFULLNbrs.setStatus(_A)
_VlanSflspLSPStatsNumIntfs_Type=Integer32
_VlanSflspLSPStatsNumIntfs_Object=MibScalar
vlanSflspLSPStatsNumIntfs=_VlanSflspLSPStatsNumIntfs_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,11),_VlanSflspLSPStatsNumIntfs_Type())
vlanSflspLSPStatsNumIntfs.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsNumIntfs.setStatus(_A)
_VlanSflspLSPStatsNum1stHops_Type=Integer32
_VlanSflspLSPStatsNum1stHops_Object=MibScalar
vlanSflspLSPStatsNum1stHops=_VlanSflspLSPStatsNum1stHops_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,12),_VlanSflspLSPStatsNum1stHops_Type())
vlanSflspLSPStatsNum1stHops.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsNum1stHops.setStatus(_A)
_VlanSflspLSPStatsNumUpdates_Type=Integer32
_VlanSflspLSPStatsNumUpdates_Object=MibScalar
vlanSflspLSPStatsNumUpdates=_VlanSflspLSPStatsNumUpdates_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,13),_VlanSflspLSPStatsNumUpdates_Type())
vlanSflspLSPStatsNumUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsNumUpdates.setStatus(_A)
_VlanSflspLSPStatsLastUpdateRecvd_Type=TimeTicks
_VlanSflspLSPStatsLastUpdateRecvd_Object=MibScalar
vlanSflspLSPStatsLastUpdateRecvd=_VlanSflspLSPStatsLastUpdateRecvd_Object((1,3,6,1,4,1,52,4,2,12,1,2,7,21,14),_VlanSflspLSPStatsLastUpdateRecvd_Type())
vlanSflspLSPStatsLastUpdateRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSflspLSPStatsLastUpdateRecvd.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'SfpsAddress':SfpsAddress,'vlanSflspGeneralSwitchID':vlanSflspGeneralSwitchID,'vlanSflspGeneralAdminStatus':vlanSflspGeneralAdminStatus,'vlanSflspGeneralVersion':vlanSflspGeneralVersion,'vlanSflspGeneralAreaBRStatus':vlanSflspGeneralAreaBRStatus,'vlanSflspGeneralASBRStatus':vlanSflspGeneralASBRStatus,'vlanSflspGeneralTOSSupport':vlanSflspGeneralTOSSupport,'vlanSflspGeneralOrgNewLSAs':vlanSflspGeneralOrgNewLSAs,'vlanSflspGeneralRcvNewLSAs':vlanSflspGeneralRcvNewLSAs,'vlanSflspGeneralMaxOnQueue':vlanSflspGeneralMaxOnQueue,'vlanSflspGeneralCurOnQueue':vlanSflspGeneralCurOnQueue,'vlanSflspGeneralMaxTimeUs':vlanSflspGeneralMaxTimeUs,'vlanSflspGeneralCurTimeUs':vlanSflspGeneralCurTimeUs,'vlanSflspGeneralMaxEvents':vlanSflspGeneralMaxEvents,'vlanSflspGeneralMaxTimeOccurred':vlanSflspGeneralMaxTimeOccurred,'vlanSflspGeneralMaxOnQOccurred':vlanSflspGeneralMaxOnQOccurred,'vlanSflspGeneralTotalSwLinks':vlanSflspGeneralTotalSwLinks,'vlanSflspGeneralLastChangeDet':vlanSflspGeneralLastChangeDet,'vlanSflspGeneralFloodMask':vlanSflspGeneralFloodMask,'vlanSflspGeneralLowestMac':vlanSflspGeneralLowestMac,'vlanSflspGeneralRootId':vlanSflspGeneralRootId,'vlanSflspGeneralFloodAdminStatus':vlanSflspGeneralFloodAdminStatus,'vlanSflspLsdbTable':vlanSflspLsdbTable,'vlanSflspLsdbEntry':vlanSflspLsdbEntry,_L:vlanSflspLsdbAreaID,_M:vlanSflspLsdbType,_N:vlanSflspLsdbLSID,_O:vlanSflspLsdbSwitchID,'vlanSflspLsdbSequence':vlanSflspLsdbSequence,'vlanSflspLsdbAge':vlanSflspLsdbAge,'vlanSflspLsdbChecksum':vlanSflspLsdbChecksum,'vlanSflspLsdbAdvertisement':vlanSflspLsdbAdvertisement,'vlanSflspLsdbUsedInSPF':vlanSflspLsdbUsedInSPF,'vlanSflspInterfacesTable':vlanSflspInterfacesTable,'vlanSflspInterfacesEntry':vlanSflspInterfacesEntry,_P:vlanSflspInterfacesIFAddress,_Q:vlanSflspInterfacesSwAddressLess,'vlanSflspInterfacesAreaID':vlanSflspInterfacesAreaID,'vlanSflspInterfacesIfType':vlanSflspInterfacesIfType,'vlanSflspInterfacesAdminStatus':vlanSflspInterfacesAdminStatus,'vlanSflspInterfacesSwPriority':vlanSflspInterfacesSwPriority,'vlanSflspInterfacesTransDelay':vlanSflspInterfacesTransDelay,'vlanSflspInterfacesReTransInterval':vlanSflspInterfacesReTransInterval,'vlanSflspInterfacesHelloInterval':vlanSflspInterfacesHelloInterval,'vlanSflspInterfacesDeadInterval':vlanSflspInterfacesDeadInterval,'vlanSflspInterfacesPollInterval':vlanSflspInterfacesPollInterval,'vlanSflspInterfacesState':vlanSflspInterfacesState,'vlanSflspInterfacesDS':vlanSflspInterfacesDS,'vlanSflspInterfacesBDS':vlanSflspInterfacesBDS,'vlanSflspInterfacesEvents':vlanSflspInterfacesEvents,'vlanSflspInterfacesAuthKey':vlanSflspInterfacesAuthKey,'vlanSflspIfMetricTable':vlanSflspIfMetricTable,'vlanSflspIfMetricEntry':vlanSflspIfMetricEntry,_S:vlanSflspIfMetricIfAddress,_T:vlanSflspIfMetricIfTOSType,'vlanSflspIfMetricIfMetric':vlanSflspIfMetricIfMetric,'vlanSflspIfMetricIfStatus':vlanSflspIfMetricIfStatus,'vlanSflspNeighborsTable':vlanSflspNeighborsTable,'vlanSflspNeighborsEntry':vlanSflspNeighborsEntry,_U:vlanSflspNeighborsPortName,'vlanSflspNeighborsSwitchID':vlanSflspNeighborsSwitchID,'vlanSflspNeighborsOptions':vlanSflspNeighborsOptions,'vlanSflspNeighborsPriority':vlanSflspNeighborsPriority,'vlanSflspNeighborsState':vlanSflspNeighborsState,'vlanSflspNeighborsEvents':vlanSflspNeighborsEvents,'vlanSflspNeighborsLSRetransQLen':vlanSflspNeighborsLSRetransQLen,'vlanSflspNeighborsHELLOsRcvd':vlanSflspNeighborsHELLOsRcvd,'vlanSflspNeighborsDBDsRcvd':vlanSflspNeighborsDBDsRcvd,'vlanSflspNeighborsLSUsRcvd':vlanSflspNeighborsLSUsRcvd,'vlanSflspNeighborsLSRsRcvd':vlanSflspNeighborsLSRsRcvd,'vlanSflspNeighborsLSACKsRcvd':vlanSflspNeighborsLSACKsRcvd,'vlanSflspNeighborsHELLOsSent':vlanSflspNeighborsHELLOsSent,'vlanSflspNeighborsDBDsSent':vlanSflspNeighborsDBDsSent,'vlanSflspNeighborsLSUsSent':vlanSflspNeighborsLSUsSent,'vlanSflspNeighborsLSRsSent':vlanSflspNeighborsLSRsSent,'vlanSflspNeighborsLSACKsSent':vlanSflspNeighborsLSACKsSent,'vlanSflspNeighborsNBMAStatus':vlanSflspNeighborsNBMAStatus,'vlanSflspNeighborsFULLTimeSec':vlanSflspNeighborsFULLTimeSec,'vlanSflspAreaTable':vlanSflspAreaTable,'vlanSflspAreaEntry':vlanSflspAreaEntry,_V:vlanSflspAreaAreaID,'vlanSflspAreaAuthType':vlanSflspAreaAuthType,'vlanSflspAreaSPFRuns':vlanSflspAreaSPFRuns,'vlanSflspAreaABRCount':vlanSflspAreaABRCount,'vlanSflspAreaASBRCount':vlanSflspAreaASBRCount,'vlanSflspAreaAreaLSACnt':vlanSflspAreaAreaLSACnt,'vlanSflspAreaAreaCheckSum':vlanSflspAreaAreaCheckSum,'vlanSflspAreaLastSpfRun':vlanSflspAreaLastSpfRun,'vlanSflsp1stHopTable':vlanSflsp1stHopTable,'vlanSflsp1stHopEntry':vlanSflsp1stHopEntry,_W:vlanSflsp1stHopDestSwitch,'vlanSflsp1stHopPath11stHop':vlanSflsp1stHopPath11stHop,'vlanSflsp1stHopPath21stHop':vlanSflsp1stHopPath21stHop,'vlanSflsp1stHopPath31stHop':vlanSflsp1stHopPath31stHop,'vlanSflspTracePathAPIDest':vlanSflspTracePathAPIDest,'vlanSflspTracePathAPIID':vlanSflspTracePathAPIID,'vlanSflspTracePathAPIType':vlanSflspTracePathAPIType,'vlanSflspTracePathAPIAction':vlanSflspTracePathAPIAction,'vlanSflspTracePathTable':vlanSflspTracePathTable,'vlanSflspTracePathEntry':vlanSflspTracePathEntry,_Z:vlanSflspTracePathDest,_a:vlanSflspTracePathID,'vlanSflspTracePathAction':vlanSflspTracePathAction,'vlanSflspTracePathStatus':vlanSflspTracePathStatus,'vlanSflspTracePathListTable':vlanSflspTracePathListTable,'vlanSflspTracePathListEntry':vlanSflspTracePathListEntry,_b:vlanSflspTracePathListDest,_c:vlanSflspTracePathListID,_d:vlanSflspTracePathListPathNum,_e:vlanSflspTracePathListHopNum,'vlanSflspTracePathListHopAddr':vlanSflspTracePathListHopAddr,'vlanSflspLSDBFloodTable':vlanSflspLSDBFloodTable,'vlanSflspLSDBFloodEntry':vlanSflspLSDBFloodEntry,_f:vlanSflspLSDBFloodAreaID,_g:vlanSflspLSDBFloodType,_h:vlanSflspLSDBFloodLSID,_i:vlanSflspLSDBFloodAdvSwitchID,'vlanSflspLSDBFloodSequence':vlanSflspLSDBFloodSequence,'vlanSflspLSDBFloodAge':vlanSflspLSDBFloodAge,'vlanSflspLSDBFloodChecksum':vlanSflspLSDBFloodChecksum,'vlanSflspLSDBFloodAdvertisement':vlanSflspLSDBFloodAdvertisement,'vlanSflspLSDBFloodUsedInSPF':vlanSflspLSDBFloodUsedInSPF,'vlanSflspLSDBFloodEverUsed':vlanSflspLSDBFloodEverUsed,'vlanSflspLSPStatsMaxOnQueue':vlanSflspLSPStatsMaxOnQueue,'vlanSflspLSPStatsCurOnQueue':vlanSflspLSPStatsCurOnQueue,'vlanSflspLSPStatsMaxTimeUs':vlanSflspLSPStatsMaxTimeUs,'vlanSflspLSPStatsCurTimeUs':vlanSflspLSPStatsCurTimeUs,'vlanSflspLSPStatsMaxTimeOccurred':vlanSflspLSPStatsMaxTimeOccurred,'vlanSflspLSPStatsMaxOnQOccurred':vlanSflspLSPStatsMaxOnQOccurred,'vlanSflspLSPStatsTotalSwLinks':vlanSflspLSPStatsTotalSwLinks,'vlanSflspLSPStatsLastChangeDet':vlanSflspLSPStatsLastChangeDet,'vlanSflspLSPStatsNumSPFRuns':vlanSflspLSPStatsNumSPFRuns,'vlanSflspLSPStatsNumFULLNbrs':vlanSflspLSPStatsNumFULLNbrs,'vlanSflspLSPStatsNumIntfs':vlanSflspLSPStatsNumIntfs,'vlanSflspLSPStatsNum1stHops':vlanSflspLSPStatsNum1stHops,'vlanSflspLSPStatsNumUpdates':vlanSflspLSPStatsNumUpdates,'vlanSflspLSPStatsLastUpdateRecvd':vlanSflspLSPStatsLastUpdateRecvd})