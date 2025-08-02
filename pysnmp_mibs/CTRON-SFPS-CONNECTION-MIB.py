_X='atm-vpi-vci'
_W='mac-da-sa'
_V='reapCnxsGivenMac'
_U='sfpsConnectionSource'
_T='sfpsConnectionDestination'
_S='netport-filter'
_R='filter'
_Q='enabled'
_P='disabled'
_O='under-creation'
_N='activate'
_M='CTRON-SFPS-CONNECTION-MIB'
_L='mcast'
_K='tap'
_J='vlan'
_I='self-prog-non-filter'
_H='delete'
_G='switched'
_F='provisioned'
_E='other'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsCNXPacketStats,sfpsConnectionAPI,sfpsConnectionConfigAPI,sfpsConnectionLookupAPI,sfpsConnectionQueryAPI,sfpsConnectionStats,sfpsConnectionTestAPI,sfpsSwitchConnections=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsCNXPacketStats','sfpsConnectionAPI','sfpsConnectionConfigAPI','sfpsConnectionLookupAPI','sfpsConnectionQueryAPI','sfpsConnectionStats','sfpsConnectionTestAPI','sfpsSwitchConnections')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SfpsSwitchPort(Integer32):0
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SfpsConnectionTable_Object=MibTable
sfpsConnectionTable=_SfpsConnectionTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1))
if mibBuilder.loadTexts:sfpsConnectionTable.setStatus(_A)
_SfpsConnectionEntry_Object=MibTableRow
sfpsConnectionEntry=_SfpsConnectionEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1))
sfpsConnectionEntry.setIndexNames((0,_M,_T),(0,_M,_U))
if mibBuilder.loadTexts:sfpsConnectionEntry.setStatus(_A)
_SfpsConnectionDestination_Type=SfpsAddress
_SfpsConnectionDestination_Object=MibTableColumn
sfpsConnectionDestination=_SfpsConnectionDestination_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,1),_SfpsConnectionDestination_Type())
sfpsConnectionDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionDestination.setStatus(_A)
_SfpsConnectionSource_Type=SfpsAddress
_SfpsConnectionSource_Object=MibTableColumn
sfpsConnectionSource=_SfpsConnectionSource_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,2),_SfpsConnectionSource_Type())
sfpsConnectionSource.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionSource.setStatus(_A)
_SfpsConnectionPrimInPort_Type=Integer32
_SfpsConnectionPrimInPort_Object=MibTableColumn
sfpsConnectionPrimInPort=_SfpsConnectionPrimInPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,3),_SfpsConnectionPrimInPort_Type())
sfpsConnectionPrimInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionPrimInPort.setStatus(_A)
_SfpsConnectionPrimOutPort_Type=Integer32
_SfpsConnectionPrimOutPort_Object=MibTableColumn
sfpsConnectionPrimOutPort=_SfpsConnectionPrimOutPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,4),_SfpsConnectionPrimOutPort_Type())
sfpsConnectionPrimOutPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionPrimOutPort.setStatus(_A)
_SfpsConnectionSecInPort_Type=Integer32
_SfpsConnectionSecInPort_Object=MibTableColumn
sfpsConnectionSecInPort=_SfpsConnectionSecInPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,5),_SfpsConnectionSecInPort_Type())
sfpsConnectionSecInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionSecInPort.setStatus(_A)
_SfpsConnectionSecOutPort_Type=Integer32
_SfpsConnectionSecOutPort_Object=MibTableColumn
sfpsConnectionSecOutPort=_SfpsConnectionSecOutPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,6),_SfpsConnectionSecOutPort_Type())
sfpsConnectionSecOutPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionSecOutPort.setStatus(_A)
class _SfpsConnectionCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_N,2),(_H,3),(_O,4)))
_SfpsConnectionCtrlStatus_Type.__name__=_D
_SfpsConnectionCtrlStatus_Object=MibTableColumn
sfpsConnectionCtrlStatus=_SfpsConnectionCtrlStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,7),_SfpsConnectionCtrlStatus_Type())
sfpsConnectionCtrlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionCtrlStatus.setStatus(_A)
class _SfpsConnectionAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_P,2),(_Q,3)))
_SfpsConnectionAdminStatus_Type.__name__=_D
_SfpsConnectionAdminStatus_Object=MibTableColumn
sfpsConnectionAdminStatus=_SfpsConnectionAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,8),_SfpsConnectionAdminStatus_Type())
sfpsConnectionAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionAdminStatus.setStatus(_A)
_SfpsConnectionAge_Type=TimeTicks
_SfpsConnectionAge_Object=MibTableColumn
sfpsConnectionAge=_SfpsConnectionAge_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,9),_SfpsConnectionAge_Type())
sfpsConnectionAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionAge.setStatus(_A)
class _SfpsConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_R,1),(_F,2),(_G,3),(_S,4),(_I,5),(_J,6),(_K,7),(_L,8)))
_SfpsConnectionType_Type.__name__=_D
_SfpsConnectionType_Object=MibTableColumn
sfpsConnectionType=_SfpsConnectionType_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,10),_SfpsConnectionType_Type())
sfpsConnectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionType.setStatus(_A)
_SfpsConnectionPkts_Type=Counter32
_SfpsConnectionPkts_Object=MibTableColumn
sfpsConnectionPkts=_SfpsConnectionPkts_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,11),_SfpsConnectionPkts_Type())
sfpsConnectionPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionPkts.setStatus(_A)
_SfpsConnectionBytes_Type=Counter32
_SfpsConnectionBytes_Object=MibTableColumn
sfpsConnectionBytes=_SfpsConnectionBytes_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,12),_SfpsConnectionBytes_Type())
sfpsConnectionBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionBytes.setStatus(_A)
_SfpsConnectionCanAge_Type=Integer32
_SfpsConnectionCanAge_Object=MibTableColumn
sfpsConnectionCanAge=_SfpsConnectionCanAge_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,13),_SfpsConnectionCanAge_Type())
sfpsConnectionCanAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionCanAge.setStatus(_A)
_SfpsConnectionPrimOutPorts_Type=DisplayString
_SfpsConnectionPrimOutPorts_Object=MibTableColumn
sfpsConnectionPrimOutPorts=_SfpsConnectionPrimOutPorts_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,14),_SfpsConnectionPrimOutPorts_Type())
sfpsConnectionPrimOutPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionPrimOutPorts.setStatus(_A)
_SfpsConnectionSecOutPorts_Type=DisplayString
_SfpsConnectionSecOutPorts_Object=MibTableColumn
sfpsConnectionSecOutPorts=_SfpsConnectionSecOutPorts_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,1,1,15),_SfpsConnectionSecOutPorts_Type())
sfpsConnectionSecOutPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionSecOutPorts.setStatus(_A)
class _SfpsConnectionLookupAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('getEntry',1))
_SfpsConnectionLookupAPIVerb_Type.__name__=_D
_SfpsConnectionLookupAPIVerb_Object=MibScalar
sfpsConnectionLookupAPIVerb=_SfpsConnectionLookupAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,1),_SfpsConnectionLookupAPIVerb_Type())
sfpsConnectionLookupAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionLookupAPIVerb.setStatus(_A)
_SfpsConnectionLookupAPIMacAddr_Type=SfpsAddress
_SfpsConnectionLookupAPIMacAddr_Object=MibScalar
sfpsConnectionLookupAPIMacAddr=_SfpsConnectionLookupAPIMacAddr_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,2),_SfpsConnectionLookupAPIMacAddr_Type())
sfpsConnectionLookupAPIMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionLookupAPIMacAddr.setStatus(_A)
_SfpsConnectionLookupAPIDestAddr_Type=SfpsAddress
_SfpsConnectionLookupAPIDestAddr_Object=MibScalar
sfpsConnectionLookupAPIDestAddr=_SfpsConnectionLookupAPIDestAddr_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,3),_SfpsConnectionLookupAPIDestAddr_Type())
sfpsConnectionLookupAPIDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPIDestAddr.setStatus(_A)
_SfpsConnectionLookupAPISourceAddr_Type=SfpsAddress
_SfpsConnectionLookupAPISourceAddr_Object=MibScalar
sfpsConnectionLookupAPISourceAddr=_SfpsConnectionLookupAPISourceAddr_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,4),_SfpsConnectionLookupAPISourceAddr_Type())
sfpsConnectionLookupAPISourceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPISourceAddr.setStatus(_A)
_SfpsConnectionLookupAPIPrimInPort_Type=Integer32
_SfpsConnectionLookupAPIPrimInPort_Object=MibScalar
sfpsConnectionLookupAPIPrimInPort=_SfpsConnectionLookupAPIPrimInPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,5),_SfpsConnectionLookupAPIPrimInPort_Type())
sfpsConnectionLookupAPIPrimInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPIPrimInPort.setStatus(_A)
_SfpsConnectionLookupAPIPrimOutPort_Type=Integer32
_SfpsConnectionLookupAPIPrimOutPort_Object=MibScalar
sfpsConnectionLookupAPIPrimOutPort=_SfpsConnectionLookupAPIPrimOutPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,6),_SfpsConnectionLookupAPIPrimOutPort_Type())
sfpsConnectionLookupAPIPrimOutPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPIPrimOutPort.setStatus(_A)
_SfpsConnectionLookupAPISecInPort_Type=Integer32
_SfpsConnectionLookupAPISecInPort_Object=MibScalar
sfpsConnectionLookupAPISecInPort=_SfpsConnectionLookupAPISecInPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,7),_SfpsConnectionLookupAPISecInPort_Type())
sfpsConnectionLookupAPISecInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPISecInPort.setStatus(_A)
_SfpsConnectionLookupAPISecOutPort_Type=Integer32
_SfpsConnectionLookupAPISecOutPort_Object=MibScalar
sfpsConnectionLookupAPISecOutPort=_SfpsConnectionLookupAPISecOutPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,8),_SfpsConnectionLookupAPISecOutPort_Type())
sfpsConnectionLookupAPISecOutPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPISecOutPort.setStatus(_A)
class _SfpsConnectionLookupAPICtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_N,2),(_H,3),(_O,4)))
_SfpsConnectionLookupAPICtrlStatus_Type.__name__=_D
_SfpsConnectionLookupAPICtrlStatus_Object=MibScalar
sfpsConnectionLookupAPICtrlStatus=_SfpsConnectionLookupAPICtrlStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,9),_SfpsConnectionLookupAPICtrlStatus_Type())
sfpsConnectionLookupAPICtrlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPICtrlStatus.setStatus(_A)
class _SfpsConnectionLookupAPIAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_P,2),(_Q,3)))
_SfpsConnectionLookupAPIAdminStatus_Type.__name__=_D
_SfpsConnectionLookupAPIAdminStatus_Object=MibScalar
sfpsConnectionLookupAPIAdminStatus=_SfpsConnectionLookupAPIAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,10),_SfpsConnectionLookupAPIAdminStatus_Type())
sfpsConnectionLookupAPIAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPIAdminStatus.setStatus(_A)
_SfpsConnectionLookupAPIAge_Type=TimeTicks
_SfpsConnectionLookupAPIAge_Object=MibScalar
sfpsConnectionLookupAPIAge=_SfpsConnectionLookupAPIAge_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,11),_SfpsConnectionLookupAPIAge_Type())
sfpsConnectionLookupAPIAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPIAge.setStatus(_A)
class _SfpsConnectionLookupAPIType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),('self-prog-filter',4),(_I,5),(_J,6),(_K,7),(_L,8),('flood',9)))
_SfpsConnectionLookupAPIType_Type.__name__=_D
_SfpsConnectionLookupAPIType_Object=MibScalar
sfpsConnectionLookupAPIType=_SfpsConnectionLookupAPIType_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,12),_SfpsConnectionLookupAPIType_Type())
sfpsConnectionLookupAPIType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPIType.setStatus(_A)
_SfpsConnectionLookupAPIPkts_Type=Integer32
_SfpsConnectionLookupAPIPkts_Object=MibScalar
sfpsConnectionLookupAPIPkts=_SfpsConnectionLookupAPIPkts_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,13),_SfpsConnectionLookupAPIPkts_Type())
sfpsConnectionLookupAPIPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPIPkts.setStatus(_A)
_SfpsConnectionLookupAPIBytes_Type=Integer32
_SfpsConnectionLookupAPIBytes_Object=MibScalar
sfpsConnectionLookupAPIBytes=_SfpsConnectionLookupAPIBytes_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,14),_SfpsConnectionLookupAPIBytes_Type())
sfpsConnectionLookupAPIBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPIBytes.setStatus(_A)
_SfpsConnectionLookupAPICanAge_Type=Integer32
_SfpsConnectionLookupAPICanAge_Object=MibScalar
sfpsConnectionLookupAPICanAge=_SfpsConnectionLookupAPICanAge_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,15),_SfpsConnectionLookupAPICanAge_Type())
sfpsConnectionLookupAPICanAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPICanAge.setStatus(_A)
_SfpsConnectionLookupAPIPrimOutPorts_Type=DisplayString
_SfpsConnectionLookupAPIPrimOutPorts_Object=MibScalar
sfpsConnectionLookupAPIPrimOutPorts=_SfpsConnectionLookupAPIPrimOutPorts_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,16),_SfpsConnectionLookupAPIPrimOutPorts_Type())
sfpsConnectionLookupAPIPrimOutPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPIPrimOutPorts.setStatus(_A)
_SfpsConnectionLookupAPISecOutPorts_Type=DisplayString
_SfpsConnectionLookupAPISecOutPorts_Object=MibScalar
sfpsConnectionLookupAPISecOutPorts=_SfpsConnectionLookupAPISecOutPorts_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,2,17),_SfpsConnectionLookupAPISecOutPorts_Type())
sfpsConnectionLookupAPISecOutPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionLookupAPISecOutPorts.setStatus(_A)
class _SfpsConnectionConfigAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('agePartial',1),('ageFull',2),('setParameter',3),('ageFilters',4),('stopAging',5)))
_SfpsConnectionConfigAPIVerb_Type.__name__=_D
_SfpsConnectionConfigAPIVerb_Object=MibScalar
sfpsConnectionConfigAPIVerb=_SfpsConnectionConfigAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,1),_SfpsConnectionConfigAPIVerb_Type())
sfpsConnectionConfigAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionConfigAPIVerb.setStatus(_A)
class _SfpsConnectionConfigAPICnxHiMark_Type(Integer32):defaultValue=95
_SfpsConnectionConfigAPICnxHiMark_Type.__name__=_D
_SfpsConnectionConfigAPICnxHiMark_Object=MibScalar
sfpsConnectionConfigAPICnxHiMark=_SfpsConnectionConfigAPICnxHiMark_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,2),_SfpsConnectionConfigAPICnxHiMark_Type())
sfpsConnectionConfigAPICnxHiMark.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionConfigAPICnxHiMark.setStatus(_A)
class _SfpsConnectionConfigAPICnxNumToAge_Type(Integer32):defaultValue=100
_SfpsConnectionConfigAPICnxNumToAge_Type.__name__=_D
_SfpsConnectionConfigAPICnxNumToAge_Object=MibScalar
sfpsConnectionConfigAPICnxNumToAge=_SfpsConnectionConfigAPICnxNumToAge_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,3),_SfpsConnectionConfigAPICnxNumToAge_Type())
sfpsConnectionConfigAPICnxNumToAge.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionConfigAPICnxNumToAge.setStatus(_A)
class _SfpsConnectionConfigAPIAgePeriod_Type(Integer32):defaultValue=0
_SfpsConnectionConfigAPIAgePeriod_Type.__name__=_D
_SfpsConnectionConfigAPIAgePeriod_Object=MibScalar
sfpsConnectionConfigAPIAgePeriod=_SfpsConnectionConfigAPIAgePeriod_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,4),_SfpsConnectionConfigAPIAgePeriod_Type())
sfpsConnectionConfigAPIAgePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionConfigAPIAgePeriod.setStatus(_A)
_SfpsConnectionConfigAPIAgePassInProgress_Type=Integer32
_SfpsConnectionConfigAPIAgePassInProgress_Object=MibScalar
sfpsConnectionConfigAPIAgePassInProgress=_SfpsConnectionConfigAPIAgePassInProgress_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,5),_SfpsConnectionConfigAPIAgePassInProgress_Type())
sfpsConnectionConfigAPIAgePassInProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionConfigAPIAgePassInProgress.setStatus(_A)
_SfpsConnectionConfigAPICurCapacity_Type=Integer32
_SfpsConnectionConfigAPICurCapacity_Object=MibScalar
sfpsConnectionConfigAPICurCapacity=_SfpsConnectionConfigAPICurCapacity_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,6),_SfpsConnectionConfigAPICurCapacity_Type())
sfpsConnectionConfigAPICurCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionConfigAPICurCapacity.setStatus(_A)
_SfpsConnectionConfigAPILastPassTime_Type=TimeTicks
_SfpsConnectionConfigAPILastPassTime_Object=MibScalar
sfpsConnectionConfigAPILastPassTime=_SfpsConnectionConfigAPILastPassTime_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,7),_SfpsConnectionConfigAPILastPassTime_Type())
sfpsConnectionConfigAPILastPassTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionConfigAPILastPassTime.setStatus(_A)
_SfpsConnectionConfigAPITimeSinceLastPass_Type=TimeTicks
_SfpsConnectionConfigAPITimeSinceLastPass_Object=MibScalar
sfpsConnectionConfigAPITimeSinceLastPass=_SfpsConnectionConfigAPITimeSinceLastPass_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,8),_SfpsConnectionConfigAPITimeSinceLastPass_Type())
sfpsConnectionConfigAPITimeSinceLastPass.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionConfigAPITimeSinceLastPass.setStatus(_A)
_SfpsConnectionConfigAPIAgePassDelta_Type=TimeTicks
_SfpsConnectionConfigAPIAgePassDelta_Object=MibScalar
sfpsConnectionConfigAPIAgePassDelta=_SfpsConnectionConfigAPIAgePassDelta_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,9),_SfpsConnectionConfigAPIAgePassDelta_Type())
sfpsConnectionConfigAPIAgePassDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionConfigAPIAgePassDelta.setStatus(_A)
_SfpsConnectionConfigAPIAgePassCount_Type=Integer32
_SfpsConnectionConfigAPIAgePassCount_Object=MibScalar
sfpsConnectionConfigAPIAgePassCount=_SfpsConnectionConfigAPIAgePassCount_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,10),_SfpsConnectionConfigAPIAgePassCount_Type())
sfpsConnectionConfigAPIAgePassCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionConfigAPIAgePassCount.setStatus(_A)
_SfpsConnectionConfigAPIAgeStatsHiMark_Type=Integer32
_SfpsConnectionConfigAPIAgeStatsHiMark_Object=MibScalar
sfpsConnectionConfigAPIAgeStatsHiMark=_SfpsConnectionConfigAPIAgeStatsHiMark_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,11),_SfpsConnectionConfigAPIAgeStatsHiMark_Type())
sfpsConnectionConfigAPIAgeStatsHiMark.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionConfigAPIAgeStatsHiMark.setStatus(_A)
_SfpsConnectionConfigAPIStatsAgingEnable_Type=Integer32
_SfpsConnectionConfigAPIStatsAgingEnable_Object=MibScalar
sfpsConnectionConfigAPIStatsAgingEnable=_SfpsConnectionConfigAPIStatsAgingEnable_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,12),_SfpsConnectionConfigAPIStatsAgingEnable_Type())
sfpsConnectionConfigAPIStatsAgingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionConfigAPIStatsAgingEnable.setStatus(_A)
_SfpsConnectionConfigAPIAgeStatsAgingSupported_Type=Integer32
_SfpsConnectionConfigAPIAgeStatsAgingSupported_Object=MibScalar
sfpsConnectionConfigAPIAgeStatsAgingSupported=_SfpsConnectionConfigAPIAgeStatsAgingSupported_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,13),_SfpsConnectionConfigAPIAgeStatsAgingSupported_Type())
sfpsConnectionConfigAPIAgeStatsAgingSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionConfigAPIAgeStatsAgingSupported.setStatus(_A)
_SfpsConnectionConfigAPIIdleCnxs_Type=Integer32
_SfpsConnectionConfigAPIIdleCnxs_Object=MibScalar
sfpsConnectionConfigAPIIdleCnxs=_SfpsConnectionConfigAPIIdleCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,14),_SfpsConnectionConfigAPIIdleCnxs_Type())
sfpsConnectionConfigAPIIdleCnxs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionConfigAPIIdleCnxs.setStatus(_A)
_SfpsConnectionConfigAPIActiveCnxs_Type=Integer32
_SfpsConnectionConfigAPIActiveCnxs_Object=MibScalar
sfpsConnectionConfigAPIActiveCnxs=_SfpsConnectionConfigAPIActiveCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,3,15),_SfpsConnectionConfigAPIActiveCnxs_Type())
sfpsConnectionConfigAPIActiveCnxs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionConfigAPIActiveCnxs.setStatus(_A)
_SfpsConnectionStatsMaxCnxs_Type=Integer32
_SfpsConnectionStatsMaxCnxs_Object=MibScalar
sfpsConnectionStatsMaxCnxs=_SfpsConnectionStatsMaxCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,1),_SfpsConnectionStatsMaxCnxs_Type())
sfpsConnectionStatsMaxCnxs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsMaxCnxs.setStatus(_A)
_SfpsConnectionStatsTotalCnxs_Type=Integer32
_SfpsConnectionStatsTotalCnxs_Object=MibScalar
sfpsConnectionStatsTotalCnxs=_SfpsConnectionStatsTotalCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,2),_SfpsConnectionStatsTotalCnxs_Type())
sfpsConnectionStatsTotalCnxs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsTotalCnxs.setStatus(_A)
_SfpsConnectionStatsSwitchedCnxs_Type=Integer32
_SfpsConnectionStatsSwitchedCnxs_Object=MibScalar
sfpsConnectionStatsSwitchedCnxs=_SfpsConnectionStatsSwitchedCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,3),_SfpsConnectionStatsSwitchedCnxs_Type())
sfpsConnectionStatsSwitchedCnxs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsSwitchedCnxs.setStatus(_A)
_SfpsConnectionStatsVlanCnxs_Type=Integer32
_SfpsConnectionStatsVlanCnxs_Object=MibScalar
sfpsConnectionStatsVlanCnxs=_SfpsConnectionStatsVlanCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,4),_SfpsConnectionStatsVlanCnxs_Type())
sfpsConnectionStatsVlanCnxs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsVlanCnxs.setStatus(_A)
_SfpsConnectionStatsFilterCnxs_Type=Integer32
_SfpsConnectionStatsFilterCnxs_Object=MibScalar
sfpsConnectionStatsFilterCnxs=_SfpsConnectionStatsFilterCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,5),_SfpsConnectionStatsFilterCnxs_Type())
sfpsConnectionStatsFilterCnxs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsFilterCnxs.setStatus(_A)
_SfpsConnectionStatsSelfProgCnxs_Type=Integer32
_SfpsConnectionStatsSelfProgCnxs_Object=MibScalar
sfpsConnectionStatsSelfProgCnxs=_SfpsConnectionStatsSelfProgCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,6),_SfpsConnectionStatsSelfProgCnxs_Type())
sfpsConnectionStatsSelfProgCnxs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsSelfProgCnxs.setStatus(_A)
_SfpsConnectionStatsProvsnedCnxs_Type=Integer32
_SfpsConnectionStatsProvsnedCnxs_Object=MibScalar
sfpsConnectionStatsProvsnedCnxs=_SfpsConnectionStatsProvsnedCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,7),_SfpsConnectionStatsProvsnedCnxs_Type())
sfpsConnectionStatsProvsnedCnxs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsProvsnedCnxs.setStatus(_A)
_SfpsConnectionStatsTapCnxs_Type=Integer32
_SfpsConnectionStatsTapCnxs_Object=MibScalar
sfpsConnectionStatsTapCnxs=_SfpsConnectionStatsTapCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,8),_SfpsConnectionStatsTapCnxs_Type())
sfpsConnectionStatsTapCnxs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsTapCnxs.setStatus(_A)
_SfpsConnectionStatsMcastCnxs_Type=Integer32
_SfpsConnectionStatsMcastCnxs_Object=MibScalar
sfpsConnectionStatsMcastCnxs=_SfpsConnectionStatsMcastCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,9),_SfpsConnectionStatsMcastCnxs_Type())
sfpsConnectionStatsMcastCnxs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsMcastCnxs.setStatus(_A)
_SfpsConnectionStatsNetPortFilterCnxs_Type=Integer32
_SfpsConnectionStatsNetPortFilterCnxs_Object=MibScalar
sfpsConnectionStatsNetPortFilterCnxs=_SfpsConnectionStatsNetPortFilterCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,10),_SfpsConnectionStatsNetPortFilterCnxs_Type())
sfpsConnectionStatsNetPortFilterCnxs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsNetPortFilterCnxs.setStatus(_A)
_SfpsConnectionStatsNonCriticalVlans_Type=Integer32
_SfpsConnectionStatsNonCriticalVlans_Object=MibScalar
sfpsConnectionStatsNonCriticalVlans=_SfpsConnectionStatsNonCriticalVlans_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,11),_SfpsConnectionStatsNonCriticalVlans_Type())
sfpsConnectionStatsNonCriticalVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsNonCriticalVlans.setStatus(_A)
_SfpsConnectionStatsAddErrors_Type=Integer32
_SfpsConnectionStatsAddErrors_Object=MibScalar
sfpsConnectionStatsAddErrors=_SfpsConnectionStatsAddErrors_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,12),_SfpsConnectionStatsAddErrors_Type())
sfpsConnectionStatsAddErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsAddErrors.setStatus(_A)
_SfpsConnectionStatsDeleteErrors_Type=Integer32
_SfpsConnectionStatsDeleteErrors_Object=MibScalar
sfpsConnectionStatsDeleteErrors=_SfpsConnectionStatsDeleteErrors_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,4,13),_SfpsConnectionStatsDeleteErrors_Type())
sfpsConnectionStatsDeleteErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionStatsDeleteErrors.setStatus(_A)
class _SfpsConnectionQueryAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('lookup',1),('add',2),(_H,3),('mapPort',4),('unmapPort',5),(_V,6),('mapPorts',7),('unMapPorts',8)))
_SfpsConnectionQueryAPIVerb_Type.__name__=_D
_SfpsConnectionQueryAPIVerb_Object=MibScalar
sfpsConnectionQueryAPIVerb=_SfpsConnectionQueryAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,1),_SfpsConnectionQueryAPIVerb_Type())
sfpsConnectionQueryAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionQueryAPIVerb.setStatus(_A)
_SfpsConnectionQueryAPIDestAddr_Type=SfpsAddress
_SfpsConnectionQueryAPIDestAddr_Object=MibScalar
sfpsConnectionQueryAPIDestAddr=_SfpsConnectionQueryAPIDestAddr_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,2),_SfpsConnectionQueryAPIDestAddr_Type())
sfpsConnectionQueryAPIDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionQueryAPIDestAddr.setStatus(_A)
_SfpsConnectionQueryAPISourceAddr_Type=SfpsAddress
_SfpsConnectionQueryAPISourceAddr_Object=MibScalar
sfpsConnectionQueryAPISourceAddr=_SfpsConnectionQueryAPISourceAddr_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,3),_SfpsConnectionQueryAPISourceAddr_Type())
sfpsConnectionQueryAPISourceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionQueryAPISourceAddr.setStatus(_A)
_SfpsConnectionQueryAPIInPort_Type=Integer32
_SfpsConnectionQueryAPIInPort_Object=MibScalar
sfpsConnectionQueryAPIInPort=_SfpsConnectionQueryAPIInPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,4),_SfpsConnectionQueryAPIInPort_Type())
sfpsConnectionQueryAPIInPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionQueryAPIInPort.setStatus(_A)
_SfpsConnectionQueryAPIOutPort_Type=Integer32
_SfpsConnectionQueryAPIOutPort_Object=MibScalar
sfpsConnectionQueryAPIOutPort=_SfpsConnectionQueryAPIOutPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,5),_SfpsConnectionQueryAPIOutPort_Type())
sfpsConnectionQueryAPIOutPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionQueryAPIOutPort.setStatus(_A)
class _SfpsConnectionQueryAPICtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_N,2),(_H,3),(_O,4)))
_SfpsConnectionQueryAPICtrlStatus_Type.__name__=_D
_SfpsConnectionQueryAPICtrlStatus_Object=MibScalar
sfpsConnectionQueryAPICtrlStatus=_SfpsConnectionQueryAPICtrlStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,6),_SfpsConnectionQueryAPICtrlStatus_Type())
sfpsConnectionQueryAPICtrlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionQueryAPICtrlStatus.setStatus(_A)
class _SfpsConnectionQueryAPIAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_P,2),(_Q,3)))
_SfpsConnectionQueryAPIAdminStatus_Type.__name__=_D
_SfpsConnectionQueryAPIAdminStatus_Object=MibScalar
sfpsConnectionQueryAPIAdminStatus=_SfpsConnectionQueryAPIAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,7),_SfpsConnectionQueryAPIAdminStatus_Type())
sfpsConnectionQueryAPIAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionQueryAPIAdminStatus.setStatus(_A)
_SfpsConnectionQueryAPIAge_Type=Integer32
_SfpsConnectionQueryAPIAge_Object=MibScalar
sfpsConnectionQueryAPIAge=_SfpsConnectionQueryAPIAge_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,8),_SfpsConnectionQueryAPIAge_Type())
sfpsConnectionQueryAPIAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionQueryAPIAge.setStatus(_A)
class _SfpsConnectionQueryAPIQueryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_R,1),(_F,2),(_G,3),(_S,4),(_I,5),(_J,6),(_K,7),(_L,8)))
_SfpsConnectionQueryAPIQueryType_Type.__name__=_D
_SfpsConnectionQueryAPIQueryType_Object=MibScalar
sfpsConnectionQueryAPIQueryType=_SfpsConnectionQueryAPIQueryType_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,9),_SfpsConnectionQueryAPIQueryType_Type())
sfpsConnectionQueryAPIQueryType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionQueryAPIQueryType.setStatus(_A)
_SfpsConnectionQueryAPIOwner_Type=Integer32
_SfpsConnectionQueryAPIOwner_Object=MibScalar
sfpsConnectionQueryAPIOwner=_SfpsConnectionQueryAPIOwner_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,10),_SfpsConnectionQueryAPIOwner_Type())
sfpsConnectionQueryAPIOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionQueryAPIOwner.setStatus(_A)
_SfpsConnectionQueryAPIPkts_Type=Counter32
_SfpsConnectionQueryAPIPkts_Object=MibScalar
sfpsConnectionQueryAPIPkts=_SfpsConnectionQueryAPIPkts_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,11),_SfpsConnectionQueryAPIPkts_Type())
sfpsConnectionQueryAPIPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionQueryAPIPkts.setStatus(_A)
_SfpsConnectionQueryAPIBytes_Type=Counter32
_SfpsConnectionQueryAPIBytes_Object=MibScalar
sfpsConnectionQueryAPIBytes=_SfpsConnectionQueryAPIBytes_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,12),_SfpsConnectionQueryAPIBytes_Type())
sfpsConnectionQueryAPIBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionQueryAPIBytes.setStatus(_A)
_SfpsConnectionQueryAPICanAge_Type=Integer32
_SfpsConnectionQueryAPICanAge_Object=MibScalar
sfpsConnectionQueryAPICanAge=_SfpsConnectionQueryAPICanAge_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,13),_SfpsConnectionQueryAPICanAge_Type())
sfpsConnectionQueryAPICanAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionQueryAPICanAge.setStatus(_A)
_SfpsConnectionQueryAPIOutPorts_Type=DisplayString
_SfpsConnectionQueryAPIOutPorts_Object=MibScalar
sfpsConnectionQueryAPIOutPorts=_SfpsConnectionQueryAPIOutPorts_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,14),_SfpsConnectionQueryAPIOutPorts_Type())
sfpsConnectionQueryAPIOutPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionQueryAPIOutPorts.setStatus(_A)
_SfpsConnectionQueryAPIMacAddr_Type=SfpsAddress
_SfpsConnectionQueryAPIMacAddr_Object=MibScalar
sfpsConnectionQueryAPIMacAddr=_SfpsConnectionQueryAPIMacAddr_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,15),_SfpsConnectionQueryAPIMacAddr_Type())
sfpsConnectionQueryAPIMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionQueryAPIMacAddr.setStatus(_A)
_SfpsConnectionQueryAPISecInPort_Type=Integer32
_SfpsConnectionQueryAPISecInPort_Object=MibScalar
sfpsConnectionQueryAPISecInPort=_SfpsConnectionQueryAPISecInPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,16),_SfpsConnectionQueryAPISecInPort_Type())
sfpsConnectionQueryAPISecInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionQueryAPISecInPort.setStatus(_A)
_SfpsConnectionQueryAPISecOutPort_Type=Integer32
_SfpsConnectionQueryAPISecOutPort_Object=MibScalar
sfpsConnectionQueryAPISecOutPort=_SfpsConnectionQueryAPISecOutPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,17),_SfpsConnectionQueryAPISecOutPort_Type())
sfpsConnectionQueryAPISecOutPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionQueryAPISecOutPort.setStatus(_A)
_SfpsConnectionQueryAPISecOutPorts_Type=DisplayString
_SfpsConnectionQueryAPISecOutPorts_Object=MibScalar
sfpsConnectionQueryAPISecOutPorts=_SfpsConnectionQueryAPISecOutPorts_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,5,18),_SfpsConnectionQueryAPISecOutPorts_Type())
sfpsConnectionQueryAPISecOutPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsConnectionQueryAPISecOutPorts.setStatus(_A)
class _SfpsConnectionTestAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fillTable',1),('reapAllCnxs',2),(_V,3),('reapCnxsGivenPort',4)))
_SfpsConnectionTestAPIVerb_Type.__name__=_D
_SfpsConnectionTestAPIVerb_Object=MibScalar
sfpsConnectionTestAPIVerb=_SfpsConnectionTestAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,6,1),_SfpsConnectionTestAPIVerb_Type())
sfpsConnectionTestAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionTestAPIVerb.setStatus(_A)
class _SfpsConnectionTestAPIType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_R,1),(_F,2),(_G,3),(_S,4),(_I,5),(_J,6),(_K,7),(_L,8)))
_SfpsConnectionTestAPIType_Type.__name__=_D
_SfpsConnectionTestAPIType_Object=MibScalar
sfpsConnectionTestAPIType=_SfpsConnectionTestAPIType_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,6,2),_SfpsConnectionTestAPIType_Type())
sfpsConnectionTestAPIType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionTestAPIType.setStatus(_A)
_SfpsConnectionTestAPINumCnxs_Type=Integer32
_SfpsConnectionTestAPINumCnxs_Object=MibScalar
sfpsConnectionTestAPINumCnxs=_SfpsConnectionTestAPINumCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,6,3),_SfpsConnectionTestAPINumCnxs_Type())
sfpsConnectionTestAPINumCnxs.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionTestAPINumCnxs.setStatus(_A)
_SfpsConnectionTestAPIMacAddr_Type=SfpsAddress
_SfpsConnectionTestAPIMacAddr_Object=MibScalar
sfpsConnectionTestAPIMacAddr=_SfpsConnectionTestAPIMacAddr_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,6,4),_SfpsConnectionTestAPIMacAddr_Type())
sfpsConnectionTestAPIMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionTestAPIMacAddr.setStatus(_A)
_SfpsConnectionTestAPIPort_Type=Integer32
_SfpsConnectionTestAPIPort_Object=MibScalar
sfpsConnectionTestAPIPort=_SfpsConnectionTestAPIPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,3,6,5),_SfpsConnectionTestAPIPort_Type())
sfpsConnectionTestAPIPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsConnectionTestAPIPort.setStatus(_A)
class _SfpsAPIVerb_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('map',2),('unmap',3),('unmapall',4)))
_SfpsAPIVerb_Type.__name__=_D
_SfpsAPIVerb_Object=MibScalar
sfpsAPIVerb=_SfpsAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,1),_SfpsAPIVerb_Type())
sfpsAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIVerb.setStatus(_A)
_SfpsAPIInPort_Type=SfpsSwitchPort
_SfpsAPIInPort_Object=MibScalar
sfpsAPIInPort=_SfpsAPIInPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,2),_SfpsAPIInPort_Type())
sfpsAPIInPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIInPort.setStatus(_A)
class _SfpsAPIInHeaderType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_W,2),(_X,3)))
_SfpsAPIInHeaderType_Type.__name__=_D
_SfpsAPIInHeaderType_Object=MibScalar
sfpsAPIInHeaderType=_SfpsAPIInHeaderType_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,3),_SfpsAPIInHeaderType_Type())
sfpsAPIInHeaderType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIInHeaderType.setStatus(_A)
class _SfpsAPIInHeaderLength_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_SfpsAPIInHeaderLength_Type.__name__=_D
_SfpsAPIInHeaderLength_Object=MibScalar
sfpsAPIInHeaderLength=_SfpsAPIInHeaderLength_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,4),_SfpsAPIInHeaderLength_Type())
sfpsAPIInHeaderLength.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIInHeaderLength.setStatus(_A)
_SfpsAPIInHeaderValue_Type=OctetString
_SfpsAPIInHeaderValue_Object=MibScalar
sfpsAPIInHeaderValue=_SfpsAPIInHeaderValue_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,5),_SfpsAPIInHeaderValue_Type())
sfpsAPIInHeaderValue.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIInHeaderValue.setStatus(_A)
_SfpsAPIOutPort_Type=SfpsSwitchPort
_SfpsAPIOutPort_Object=MibScalar
sfpsAPIOutPort=_SfpsAPIOutPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,6),_SfpsAPIOutPort_Type())
sfpsAPIOutPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIOutPort.setStatus(_A)
class _SfpsAPIOutHeaderType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_W,2),(_X,3)))
_SfpsAPIOutHeaderType_Type.__name__=_D
_SfpsAPIOutHeaderType_Object=MibScalar
sfpsAPIOutHeaderType=_SfpsAPIOutHeaderType_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,7),_SfpsAPIOutHeaderType_Type())
sfpsAPIOutHeaderType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIOutHeaderType.setStatus(_A)
_SfpsAPIOutHeaderLength_Type=Integer32
_SfpsAPIOutHeaderLength_Object=MibScalar
sfpsAPIOutHeaderLength=_SfpsAPIOutHeaderLength_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,8),_SfpsAPIOutHeaderLength_Type())
sfpsAPIOutHeaderLength.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIOutHeaderLength.setStatus(_A)
_SfpsAPIOutHeaderValue_Type=OctetString
_SfpsAPIOutHeaderValue_Object=MibScalar
sfpsAPIOutHeaderValue=_SfpsAPIOutHeaderValue_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,9),_SfpsAPIOutHeaderValue_Type())
sfpsAPIOutHeaderValue.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIOutHeaderValue.setStatus(_A)
class _SfpsAPIArgumentDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('bi-directional',2),('uni-directional',3)))
_SfpsAPIArgumentDirection_Type.__name__=_D
_SfpsAPIArgumentDirection_Object=MibScalar
sfpsAPIArgumentDirection=_SfpsAPIArgumentDirection_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,10),_SfpsAPIArgumentDirection_Type())
sfpsAPIArgumentDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIArgumentDirection.setStatus(_A)
class _SfpsAPIArgumentOwner_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('own-the-call',2),('dont-own-the-call',3)))
_SfpsAPIArgumentOwner_Type.__name__=_D
_SfpsAPIArgumentOwner_Object=MibScalar
sfpsAPIArgumentOwner=_SfpsAPIArgumentOwner_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,11),_SfpsAPIArgumentOwner_Type())
sfpsAPIArgumentOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIArgumentOwner.setStatus(_A)
class _SfpsAPIArgumentPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),('priority-1',2),('priority-2',3),('priority-3',4),('priority-4',5),('priority-5',6)))
_SfpsAPIArgumentPriority_Type.__name__=_D
_SfpsAPIArgumentPriority_Object=MibScalar
sfpsAPIArgumentPriority=_SfpsAPIArgumentPriority_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,12),_SfpsAPIArgumentPriority_Type())
sfpsAPIArgumentPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIArgumentPriority.setStatus(_A)
class _SfpsAPIType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),('filtered',3),(_F,4)))
_SfpsAPIType_Type.__name__=_D
_SfpsAPIType_Object=MibScalar
sfpsAPIType=_SfpsAPIType_Object((1,3,6,1,4,1,52,4,2,4,2,1,4,13),_SfpsAPIType_Type())
sfpsAPIType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsAPIType.setStatus(_A)
_SfpsCNXPacketStatsVer1Tx_Type=Integer32
_SfpsCNXPacketStatsVer1Tx_Object=MibScalar
sfpsCNXPacketStatsVer1Tx=_SfpsCNXPacketStatsVer1Tx_Object((1,3,6,1,4,1,52,4,2,4,2,1,15,1),_SfpsCNXPacketStatsVer1Tx_Type())
sfpsCNXPacketStatsVer1Tx.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCNXPacketStatsVer1Tx.setStatus(_A)
_SfpsCNXPacketStatsVer2Tx_Type=Integer32
_SfpsCNXPacketStatsVer2Tx_Object=MibScalar
sfpsCNXPacketStatsVer2Tx=_SfpsCNXPacketStatsVer2Tx_Object((1,3,6,1,4,1,52,4,2,4,2,1,15,2),_SfpsCNXPacketStatsVer2Tx_Type())
sfpsCNXPacketStatsVer2Tx.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCNXPacketStatsVer2Tx.setStatus(_A)
_SfpsCNXPacketStatsVer1Rx_Type=Integer32
_SfpsCNXPacketStatsVer1Rx_Object=MibScalar
sfpsCNXPacketStatsVer1Rx=_SfpsCNXPacketStatsVer1Rx_Object((1,3,6,1,4,1,52,4,2,4,2,1,15,3),_SfpsCNXPacketStatsVer1Rx_Type())
sfpsCNXPacketStatsVer1Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCNXPacketStatsVer1Rx.setStatus(_A)
_SfpsCNXPacketStatsVer2Rx_Type=Integer32
_SfpsCNXPacketStatsVer2Rx_Object=MibScalar
sfpsCNXPacketStatsVer2Rx=_SfpsCNXPacketStatsVer2Rx_Object((1,3,6,1,4,1,52,4,2,4,2,1,15,4),_SfpsCNXPacketStatsVer2Rx_Type())
sfpsCNXPacketStatsVer2Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCNXPacketStatsVer2Rx.setStatus(_A)
_SfpsCNXPacketStatsOpCode1Tx_Type=Integer32
_SfpsCNXPacketStatsOpCode1Tx_Object=MibScalar
sfpsCNXPacketStatsOpCode1Tx=_SfpsCNXPacketStatsOpCode1Tx_Object((1,3,6,1,4,1,52,4,2,4,2,1,15,5),_SfpsCNXPacketStatsOpCode1Tx_Type())
sfpsCNXPacketStatsOpCode1Tx.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCNXPacketStatsOpCode1Tx.setStatus(_A)
_SfpsCNXPacketStatsOpCode2Tx_Type=Integer32
_SfpsCNXPacketStatsOpCode2Tx_Object=MibScalar
sfpsCNXPacketStatsOpCode2Tx=_SfpsCNXPacketStatsOpCode2Tx_Object((1,3,6,1,4,1,52,4,2,4,2,1,15,6),_SfpsCNXPacketStatsOpCode2Tx_Type())
sfpsCNXPacketStatsOpCode2Tx.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCNXPacketStatsOpCode2Tx.setStatus(_A)
_SfpsCNXPacketStatsOpCode1Rx_Type=Integer32
_SfpsCNXPacketStatsOpCode1Rx_Object=MibScalar
sfpsCNXPacketStatsOpCode1Rx=_SfpsCNXPacketStatsOpCode1Rx_Object((1,3,6,1,4,1,52,4,2,4,2,1,15,7),_SfpsCNXPacketStatsOpCode1Rx_Type())
sfpsCNXPacketStatsOpCode1Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCNXPacketStatsOpCode1Rx.setStatus(_A)
_SfpsCNXPacketStatsOpCode2Rx_Type=Integer32
_SfpsCNXPacketStatsOpCode2Rx_Object=MibScalar
sfpsCNXPacketStatsOpCode2Rx=_SfpsCNXPacketStatsOpCode2Rx_Object((1,3,6,1,4,1,52,4,2,4,2,1,15,8),_SfpsCNXPacketStatsOpCode2Rx_Type())
sfpsCNXPacketStatsOpCode2Rx.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCNXPacketStatsOpCode2Rx.setStatus(_A)
_SfpsCNXPacketStatsRxErrors_Type=Integer32
_SfpsCNXPacketStatsRxErrors_Object=MibScalar
sfpsCNXPacketStatsRxErrors=_SfpsCNXPacketStatsRxErrors_Object((1,3,6,1,4,1,52,4,2,4,2,1,15,9),_SfpsCNXPacketStatsRxErrors_Type())
sfpsCNXPacketStatsRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCNXPacketStatsRxErrors.setStatus(_A)
mibBuilder.exportSymbols(_M,**{'SfpsSwitchPort':SfpsSwitchPort,'SfpsAddress':SfpsAddress,'sfpsConnectionTable':sfpsConnectionTable,'sfpsConnectionEntry':sfpsConnectionEntry,_T:sfpsConnectionDestination,_U:sfpsConnectionSource,'sfpsConnectionPrimInPort':sfpsConnectionPrimInPort,'sfpsConnectionPrimOutPort':sfpsConnectionPrimOutPort,'sfpsConnectionSecInPort':sfpsConnectionSecInPort,'sfpsConnectionSecOutPort':sfpsConnectionSecOutPort,'sfpsConnectionCtrlStatus':sfpsConnectionCtrlStatus,'sfpsConnectionAdminStatus':sfpsConnectionAdminStatus,'sfpsConnectionAge':sfpsConnectionAge,'sfpsConnectionType':sfpsConnectionType,'sfpsConnectionPkts':sfpsConnectionPkts,'sfpsConnectionBytes':sfpsConnectionBytes,'sfpsConnectionCanAge':sfpsConnectionCanAge,'sfpsConnectionPrimOutPorts':sfpsConnectionPrimOutPorts,'sfpsConnectionSecOutPorts':sfpsConnectionSecOutPorts,'sfpsConnectionLookupAPIVerb':sfpsConnectionLookupAPIVerb,'sfpsConnectionLookupAPIMacAddr':sfpsConnectionLookupAPIMacAddr,'sfpsConnectionLookupAPIDestAddr':sfpsConnectionLookupAPIDestAddr,'sfpsConnectionLookupAPISourceAddr':sfpsConnectionLookupAPISourceAddr,'sfpsConnectionLookupAPIPrimInPort':sfpsConnectionLookupAPIPrimInPort,'sfpsConnectionLookupAPIPrimOutPort':sfpsConnectionLookupAPIPrimOutPort,'sfpsConnectionLookupAPISecInPort':sfpsConnectionLookupAPISecInPort,'sfpsConnectionLookupAPISecOutPort':sfpsConnectionLookupAPISecOutPort,'sfpsConnectionLookupAPICtrlStatus':sfpsConnectionLookupAPICtrlStatus,'sfpsConnectionLookupAPIAdminStatus':sfpsConnectionLookupAPIAdminStatus,'sfpsConnectionLookupAPIAge':sfpsConnectionLookupAPIAge,'sfpsConnectionLookupAPIType':sfpsConnectionLookupAPIType,'sfpsConnectionLookupAPIPkts':sfpsConnectionLookupAPIPkts,'sfpsConnectionLookupAPIBytes':sfpsConnectionLookupAPIBytes,'sfpsConnectionLookupAPICanAge':sfpsConnectionLookupAPICanAge,'sfpsConnectionLookupAPIPrimOutPorts':sfpsConnectionLookupAPIPrimOutPorts,'sfpsConnectionLookupAPISecOutPorts':sfpsConnectionLookupAPISecOutPorts,'sfpsConnectionConfigAPIVerb':sfpsConnectionConfigAPIVerb,'sfpsConnectionConfigAPICnxHiMark':sfpsConnectionConfigAPICnxHiMark,'sfpsConnectionConfigAPICnxNumToAge':sfpsConnectionConfigAPICnxNumToAge,'sfpsConnectionConfigAPIAgePeriod':sfpsConnectionConfigAPIAgePeriod,'sfpsConnectionConfigAPIAgePassInProgress':sfpsConnectionConfigAPIAgePassInProgress,'sfpsConnectionConfigAPICurCapacity':sfpsConnectionConfigAPICurCapacity,'sfpsConnectionConfigAPILastPassTime':sfpsConnectionConfigAPILastPassTime,'sfpsConnectionConfigAPITimeSinceLastPass':sfpsConnectionConfigAPITimeSinceLastPass,'sfpsConnectionConfigAPIAgePassDelta':sfpsConnectionConfigAPIAgePassDelta,'sfpsConnectionConfigAPIAgePassCount':sfpsConnectionConfigAPIAgePassCount,'sfpsConnectionConfigAPIAgeStatsHiMark':sfpsConnectionConfigAPIAgeStatsHiMark,'sfpsConnectionConfigAPIStatsAgingEnable':sfpsConnectionConfigAPIStatsAgingEnable,'sfpsConnectionConfigAPIAgeStatsAgingSupported':sfpsConnectionConfigAPIAgeStatsAgingSupported,'sfpsConnectionConfigAPIIdleCnxs':sfpsConnectionConfigAPIIdleCnxs,'sfpsConnectionConfigAPIActiveCnxs':sfpsConnectionConfigAPIActiveCnxs,'sfpsConnectionStatsMaxCnxs':sfpsConnectionStatsMaxCnxs,'sfpsConnectionStatsTotalCnxs':sfpsConnectionStatsTotalCnxs,'sfpsConnectionStatsSwitchedCnxs':sfpsConnectionStatsSwitchedCnxs,'sfpsConnectionStatsVlanCnxs':sfpsConnectionStatsVlanCnxs,'sfpsConnectionStatsFilterCnxs':sfpsConnectionStatsFilterCnxs,'sfpsConnectionStatsSelfProgCnxs':sfpsConnectionStatsSelfProgCnxs,'sfpsConnectionStatsProvsnedCnxs':sfpsConnectionStatsProvsnedCnxs,'sfpsConnectionStatsTapCnxs':sfpsConnectionStatsTapCnxs,'sfpsConnectionStatsMcastCnxs':sfpsConnectionStatsMcastCnxs,'sfpsConnectionStatsNetPortFilterCnxs':sfpsConnectionStatsNetPortFilterCnxs,'sfpsConnectionStatsNonCriticalVlans':sfpsConnectionStatsNonCriticalVlans,'sfpsConnectionStatsAddErrors':sfpsConnectionStatsAddErrors,'sfpsConnectionStatsDeleteErrors':sfpsConnectionStatsDeleteErrors,'sfpsConnectionQueryAPIVerb':sfpsConnectionQueryAPIVerb,'sfpsConnectionQueryAPIDestAddr':sfpsConnectionQueryAPIDestAddr,'sfpsConnectionQueryAPISourceAddr':sfpsConnectionQueryAPISourceAddr,'sfpsConnectionQueryAPIInPort':sfpsConnectionQueryAPIInPort,'sfpsConnectionQueryAPIOutPort':sfpsConnectionQueryAPIOutPort,'sfpsConnectionQueryAPICtrlStatus':sfpsConnectionQueryAPICtrlStatus,'sfpsConnectionQueryAPIAdminStatus':sfpsConnectionQueryAPIAdminStatus,'sfpsConnectionQueryAPIAge':sfpsConnectionQueryAPIAge,'sfpsConnectionQueryAPIQueryType':sfpsConnectionQueryAPIQueryType,'sfpsConnectionQueryAPIOwner':sfpsConnectionQueryAPIOwner,'sfpsConnectionQueryAPIPkts':sfpsConnectionQueryAPIPkts,'sfpsConnectionQueryAPIBytes':sfpsConnectionQueryAPIBytes,'sfpsConnectionQueryAPICanAge':sfpsConnectionQueryAPICanAge,'sfpsConnectionQueryAPIOutPorts':sfpsConnectionQueryAPIOutPorts,'sfpsConnectionQueryAPIMacAddr':sfpsConnectionQueryAPIMacAddr,'sfpsConnectionQueryAPISecInPort':sfpsConnectionQueryAPISecInPort,'sfpsConnectionQueryAPISecOutPort':sfpsConnectionQueryAPISecOutPort,'sfpsConnectionQueryAPISecOutPorts':sfpsConnectionQueryAPISecOutPorts,'sfpsConnectionTestAPIVerb':sfpsConnectionTestAPIVerb,'sfpsConnectionTestAPIType':sfpsConnectionTestAPIType,'sfpsConnectionTestAPINumCnxs':sfpsConnectionTestAPINumCnxs,'sfpsConnectionTestAPIMacAddr':sfpsConnectionTestAPIMacAddr,'sfpsConnectionTestAPIPort':sfpsConnectionTestAPIPort,'sfpsAPIVerb':sfpsAPIVerb,'sfpsAPIInPort':sfpsAPIInPort,'sfpsAPIInHeaderType':sfpsAPIInHeaderType,'sfpsAPIInHeaderLength':sfpsAPIInHeaderLength,'sfpsAPIInHeaderValue':sfpsAPIInHeaderValue,'sfpsAPIOutPort':sfpsAPIOutPort,'sfpsAPIOutHeaderType':sfpsAPIOutHeaderType,'sfpsAPIOutHeaderLength':sfpsAPIOutHeaderLength,'sfpsAPIOutHeaderValue':sfpsAPIOutHeaderValue,'sfpsAPIArgumentDirection':sfpsAPIArgumentDirection,'sfpsAPIArgumentOwner':sfpsAPIArgumentOwner,'sfpsAPIArgumentPriority':sfpsAPIArgumentPriority,'sfpsAPIType':sfpsAPIType,'sfpsCNXPacketStatsVer1Tx':sfpsCNXPacketStatsVer1Tx,'sfpsCNXPacketStatsVer2Tx':sfpsCNXPacketStatsVer2Tx,'sfpsCNXPacketStatsVer1Rx':sfpsCNXPacketStatsVer1Rx,'sfpsCNXPacketStatsVer2Rx':sfpsCNXPacketStatsVer2Rx,'sfpsCNXPacketStatsOpCode1Tx':sfpsCNXPacketStatsOpCode1Tx,'sfpsCNXPacketStatsOpCode2Tx':sfpsCNXPacketStatsOpCode2Tx,'sfpsCNXPacketStatsOpCode1Rx':sfpsCNXPacketStatsOpCode1Rx,'sfpsCNXPacketStatsOpCode2Rx':sfpsCNXPacketStatsOpCode2Rx,'sfpsCNXPacketStatsRxErrors':sfpsCNXPacketStatsRxErrors})